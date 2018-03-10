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

if __name__ == '__main__':
    LL1 = LinkedList([6, 3, 2])
    LL2 = LinkedList([8, 5])
    ll_merged = merge_ll(LL1.head, LL2.head)
