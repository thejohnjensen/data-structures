"""."""
from src.linked_list import LinkedList


class Node(object):

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def merge_ll(LL1, LL2):
    """."""
    dummy_head = tail = Node()
    while LL1 and LL2:
        if LL1.data < LL2.data:
            tail.next, LL1 = LL1, LL1.next
        else:
            tail.next, LL2 = LL2, LL2.next
        tail = tail.next
    tail.next = LL1 or LL2
    return dummy_head.next


def rev_ll(ll):
    prev, curr = None, ll.head
    temp = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        if curr is None:
            ll.head = prev


def rev_sub(ll, s, f):
    prev, curr = None, ll.head
    start, tail = None, None
    for i in range(1, f + 1):
        # import pdb; pdb.set_trace()
        if i == s - 1:
            start = curr
        if i == f:
            tail = curr.next
            start.next.next = tail
            start.next = curr
            curr.next = prev
        if i >= s and i < f:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        else:
            prev = curr
            curr = curr.next


if __name__ == '__main__':
    LL1 = LinkedList([6, 3, 2])
    LL2 = LinkedList([8, 5])
    ll_merged = merge_ll(LL1.head, LL2.head)
    ll = LinkedList([8, 7, 6, 5, 4, 3, 2, 1])
    print(ll.display())
    # rev_ll(ll)
    rev_sub(ll, 3, 5)
    print(ll.display())
