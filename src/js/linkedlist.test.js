const LinkedList = require('./linked_list');


test('linked list is created', () => {
    const ll = new LinkedList()
    expect(ll).toEqual({'head': null, 'size': 0})
})

test('head is 8', () => {
    const ll = new LinkedList()
    ll.push(8)
    expect(ll.head.val).toEqual(8)
})

test('head is 8, next is 10', () => {
    const ll = new LinkedList()
    ll.push(8)
    ll.push(10)
    expect(ll.head.val).toEqual(10)
    expect(ll.head.next.val).toEqual(8)
    expect(ll.head.next.next).toBe(null)
})

test('size returns correct number', () => {
    const ll = new LinkedList()
    for (var i = 10; i < 20; i++) {
        ll.push(i)
    }
    expect(ll.head.val).toEqual(19)
    expect(ll.size).toEqual(10)
})