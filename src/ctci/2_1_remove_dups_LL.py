from src.linked_list import LinkedList


def remove_dups(ll):
    """."""
    if ll is None:
        return None
    visited = set()
    curr = ll.head
    prev = None
    while curr:
        if curr.data in visited:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            visited.add(curr.data)
            prev = curr
            curr = curr.next
    return ll.display()


def alternating_split(head):
    """."""
    if head is None:
        return None
    forward = head.next
    back = head
    first = back
    second = forward
    while forward and back:
        if forward.next is None or back.next is None:
            back.next = None
            forward.next = None
            break
        back.next = forward.next
        back = back.next
        forward.next = back.next
        forward = back.next

    return (first, second)


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5, 6, 3, 2, 1])
    ll2 = LinkedList([2, 1])
    split = alternating_split(ll2.head)
    print(remove_dups(ll))
