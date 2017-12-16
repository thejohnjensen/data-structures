const LinkedList = require('./linked_list');

test('linked list is created', () => {
    const ll = new LinkedList()
    expect(ll).toEqual({'head': null, 'length': 0})
});

test('head is 1', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.head.val).toEqual(1)
});

test('head is 8, next is 9', () => {
    const ll = new LinkedList()
    ll.push(8)
    ll.push(9)
    expect(ll.head.val).toEqual(9)
    expect(ll.head.next.val).toEqual(8)
    expect(ll.head.next.next).toBe(null)
});

test('size returns correct number', () => {
    const ll = new LinkedList()
    for (var i = 10; i < 20; i++) {
        ll.push(i)
    }
    expect(ll.head.val).toEqual(19)
    expect(ll.length).toEqual(10)
});

test('pop returns value 1', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    popped = ll.pop()
    expect(popped).toEqual(1)
});

test('pop sets head to next node', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    ll.pop()
    expect(ll.head.val).toEqual(2)
});

test('pop decrements length', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
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
    const ll = new LinkedList([9])
    expect(ll.length).toEqual(1)
    ll.pop()
    expect(ll.length).toEqual(0)
    expect(() => {
        ll.pop();
    }).toThrowError('Your LinkedList is empty.')
});

test('search returns node', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    const node = ll.search(8)
    expect(node.val).toEqual(8)
    expect(node.next.val).toEqual(9)
});

test('search returns null', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    const node = ll.search(100)
    expect(node).toEqual(null)
});

test('remove head and test length method', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.size()).toEqual(9)
    ll.remove(1)
    expect(ll.size()).toEqual(8)
    expect(ll.head.val).toEqual(2)
});

test('remove node in middle of list', () => {
    const ll = new LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    expect(ll.size()).toEqual(9)
    expect(ll.search(4).val).toEqual(4)
    ll.remove(4)
    expect(ll.size()).toEqual(8)
    expect(ll.head.next.next.next.val).toEqual(5)
    expect(ll.search(4)).toEqual(null)
})

test('remove single node', () => {
    const ll = new LinkedList([8])
    ll.remove(8)
    expect(ll.head).toEqual(null)
})

test('display list', () => {
    const ll = new LinkedList([9, 8, 7, 6, 'hi there', 5, 4, 3, 2, 1, 'hello'])
    expect(ll.display()).toEqual([9, 8, 7, 6, 'hi there', 5, 4, 3, 2, 1, 'hello'])
})

test('display empty list', () => {
    const ll = new LinkedList([])
    expect(ll.display()).toEqual([])
})