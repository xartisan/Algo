from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    ret = []
    temp = []

    q = deque()
    q.append(root)
    last = root
    next_last = None
    current = None

    while q:
        current = q.popleft()
        temp.append(current.val)
        l_child, r_child = current.left, current.right
        if l_child is not None:
            q.append(l_child)
            next_last = l_child
        if r_child is not None:
            q.append(r_child)
            next_last = r_child
        if current is last:
            ret.append(temp)
            temp = []
            last = next_last

    return ret


def serialize(node, ret):
    if node is None:
        ret.append('#')
        ret.append('!')
        return
    val = node.val
    val_chars = str(val).split()
    ret.extend(val_chars)
    ret.append('!')
    serialize(node.left, ret)
    serialize(node.right, ret)


def deserialize(chars, start=0):
    """
    ['1','2','!','3','!','#','!','#','!','#','!']
    """
    # base case
    if len(chars) <= start:
        return None, start
    end = chars.index('!', start)
    if chars[end - 1] != '#':
        val = int(''.join(chars[start: end]))
        node = Node(val)
        node.left, start = deserialize(chars, end + 1)
        node.right, start = deserialize(chars, start)
        return node, start
    else:
        return None, end + 1


if __name__ == '__main__':
    chars = ['1', '2', '!', '3', '!', '#', '!', '#', '!', '#', '!']
    tree, _ = deserialize(chars)
    assert print_tree(tree) == [[12], [3]], 'print_tree error'
    chars_serialized = []
    serialize(tree, chars_serialized)
    assert chars == chars_serialized, 'error'
