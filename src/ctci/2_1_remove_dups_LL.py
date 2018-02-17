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


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5, 6, 3, 2, 1])
    print(remove_dups(ll))


