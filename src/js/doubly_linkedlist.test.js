const DoublyLinkedList = require('./doubly_linked_list');

test('linked list is created', () => {
    const ll = new DoublyLinkedList()
    expect(ll).toEqual({'head': null, 'length': 0, 'tail': null})
});

test('head is 1', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.head.val).toEqual(1)
});

test('head is 8, next is 9', () => {
    const ll = new DoublyLinkedList()
    ll.push(8)
    ll.push(9)
    expect(ll.head.val).toEqual(9)
    expect(ll.head.next.val).toEqual(8)
    expect(ll.head.next.next).toBe(null)
});

test('previous points to head', () => {
    const ll = new DoublyLinkedList()
    ll.push(8)
    ll.push(9)
    expect(ll.head.next.prev.val).toEqual(9)
});

test('push one node is head and tail', () => {
    const ll = new DoublyLinkedList()
    ll.push(8)
    expect(ll.head.val).toEqual(8)
    expect(ll.tail.val).toEqual(8)
})

test('pop sets prev correctly', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    popped = ll.pop()
    expect(popped).toEqual(1)
    expect(ll.head.val).toEqual(2)
    expect(ll.head.next.val).toEqual(3)
    expect(ll.head.next.prev.val).toEqual(2)
    expect(ll.head.prev).toBe(null)
    expect(ll.tail.val).toEqual(9)
})

test('pop returns value 1', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    popped = ll.pop()
    expect(popped).toEqual(1)
});

test('pop sets head to next node', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    ll.pop()
    expect(ll.head.val).toEqual(2)
});

test('pop decrements length', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.length).toEqual(9)
    ll.pop()
    expect(ll.length).toEqual(8)
    ll.pop()
    expect(ll.length).toEqual(7)
    ll.pop()
    expect(ll.length).toEqual(6)
    ll.pop()
    expect(ll.length).toEqual(5)
});

test('pop throws proper error on empty list', () => {
    const ll = new DoublyLinkedList([9])
    expect(ll.length).toEqual(1)
    ll.pop()
    expect(ll.length).toEqual(0)
    expect(() => {
        ll.pop();
    }).toThrowError('Your DoublyLinkedList is empty.')
});

test('shift returns error on empty list', () => {
    const ll = new DoublyLinkedList()
    expect(() => {
        ll.shift();
    }).toThrowError('Your DoublyLinkedList is empty.')
})

test('shift works on single list', () => {
    const ll = new DoublyLinkedList([8])
    val = ll.shift()
    expect(val).toEqual(8)
    expect(ll.head).toBe(null)
    expect(ll.tail).toBe(null)
})

test('shift works on full list', () => {
    const ll = new DoublyLinkedList([3, 2, 1])
    val = ll.shift()
    expect(val).toEqual(3)
    expect(ll.head.val).toEqual(1)
    expect(ll.tail.val).toEqual(2)
    expect(ll.head.next.val).toEqual(2)
    expect(ll.tail.next).toBe(null)
    expect(ll.tail.prev.val).toEqual(1)
})

test('append on empty list', () => {
    const ll = new DoublyLinkedList()
    ll.append(8)
    expect(ll.head.val).toEqual(8)
    expect(ll.tail.val).toEqual(8)
    expect(ll.head.next).toBe(null)
    expect(ll.head.prev).toBe(null)
})

test('append on list', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.tail.val).toEqual(9)
    ll.append(10)
    expect(ll.tail.val).toEqual(10)
    expect(ll.tail.prev.val).toEqual(9)
    expect(ll.tail.next).toBe(null)
})

test('size returns correct number', () => {
    const ll = new DoublyLinkedList()
    for (var i = 10; i < 20; i++) {
        ll.push(i)
    }
    expect(ll.head.val).toEqual(19)
    expect(ll.length).toEqual(10)
});

test('search returns node', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    const node = ll.search(8)
    expect(node.val).toEqual(8)
    expect(node.next.val).toEqual(9)
});

test('search returns null', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    const node = ll.search(100)
    expect(node).toEqual(null)
});

test('remove head and test length method', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.size()).toEqual(9)
    ll.remove(1)
    expect(ll.size()).toEqual(8)
    expect(ll.head.val).toEqual(2)
    expect(ll.head.prev).toBe(null)
    expect(ll.head.next.val).toEqual(3)
});

test('remove node in middle of list', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.size()).toEqual(9)
    expect(ll.search(4).val).toEqual(4)
    ll.remove(4)
    expect(ll.size()).toEqual(8)
    expect(ll.head.next.next.next.val).toEqual(5)
    expect(ll.head.next.next.next.prev.val).toEqual(3)
    expect(ll.search(4)).toEqual(null)
})

test('remove single node', () => {
    const ll = new DoublyLinkedList([8])
    ll.remove(8)
    expect(ll.head).toEqual(null)
})

test('remove tail', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.tail.val).toEqual(9)
    ll.remove(9)
    expect(ll.tail.val).toEqual(8)
    expect(ll.tail.next).toBe(null)
    console.log(ll.tail)
    expect(ll.tail.prev.val).toEqual(7)
})

test('display list', () => {
    const ll = new DoublyLinkedList([9, 8, 7, 6, 'hi there', 5, 4, 3, 2, 1, 'hello'])
    expect(ll.display()).toEqual([9, 8, 7, 6, 'hi there', 5, 4, 3, 2, 1, 'hello'])
})

test('display empty list', () => {
    const ll = new DoublyLinkedList([])
    expect(ll.display()).toEqual([])
})