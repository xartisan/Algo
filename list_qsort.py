# quicksort algorithms for linked list


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        rv = str(self.val)
        if self.next:
            rv = rv + ' -> ' + repr(self.next)
        return rv


def qsort(start, end=None):
    if start is end or start.next is end:
        return
    pivot = start.val
    last = start
    cur = start.next
    # partition
    while cur is not end:
        if cur.val <= pivot:
            last = last.next
            cur.val, last.val = last.val, cur.val
        cur = cur.next
    start.val, last.val = last.val, start.val

    qsort(start, last)
    qsort(last.next, end)
