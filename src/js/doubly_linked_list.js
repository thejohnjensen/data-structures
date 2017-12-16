'use strict'

class Node {
    constructor(val) {
        this.val = val
        this.next = null
        this.prev = null
    }
}

class DoublyLinkedList {
    constructor(iterable = []) {
        this.head = null
        this.tail = null
        this.length = 0
        for (var i = 0; i < iterable.length; i++) {
            this.push(iterable[i]);
        }
    }

    push(val) {
        var new_node = new Node(val)
        if(this.length === 0) {
            this.head = new_node
            this.tail = new_node
            this.length++
        } else {
            const curr = this.head
            new_node.next = curr
            curr.prev = new_node
            this.head = new_node
            this.length++
        }
    }

    append(val) {
        var new_node = new Node(val)
        if(this.length === 0) {
            this.head = new_node
            this.tail = new_node
            this.length++
        } else {
            const curr = this.tail
            new_node.prev = curr
            curr.next = new_node
            this.tail = new_node
            this.length++
        }
    }

    pop() {
        if(this.length === 0) {
            throw('Your DoublyLinkedList is empty.')
        } else if (this.length === 1) {
            const toReturn = this.head
            this.head = null
            this.tail = null
            this.length--
            return toReturn.val
        } else {
            const toReturn = this.head
            this.head = toReturn.next
            toReturn.next = null
            this.head.prev = null
            this.length--
            return toReturn.val
        }
    }

    shift() {
        if(this.length === 0) {
            throw('Your DoublyLinkedList is empty.')
        } else if (this.length === 1) {
            const toReturn = this.tail
            this.head = null
            this.tail = null
            this.length--
            return toReturn.val
        } else {
            const toReturn = this.tail
            this.tail = toReturn.prev
            toReturn.prev = null
            this.tail.next = null
            this.length--
            return toReturn.val
        }
    }

    size() {
        return this.length
    }

    search(val) {
        if(this.length === 0) {
            throw('Your DoublyLinkedList is empty.')
        } else {
            let curr = this.head
            let found = false
            while(!found) {
                if(curr.val === val) {
                    found = true
                } else if(curr.next) {
                    curr = curr.next
                } else {
                    return null
                }
            }
            return curr
        }
    }

    remove(val) {
        if(this.length === 0) {
            throw('Your DoublyLinkedList is empty.')
        } else {
            let curr = this.head
            let found = false
            if(curr.val === val) {
                let toRemove = curr
                this.head = curr.next
                if(curr.next) {
                    curr.next.prev = null
                }
                curr.next = null
                this.length--
                return
            }
            let follow = null
            while(!found) {
                if(curr.val === val) {
                    found = true
                    let toRemove = curr
                    follow.next = curr.next
                    if (curr.next) {
                        curr.next.prev = follow
                    } else {
                        this.tail = follow
                    }
                    curr.next = null
                    curr.prev = null
                    this.length--
                    return
                } else if(curr.next) {
                    follow = curr
                    curr = curr.next
                } else {
                    throw('Val not in DoublyLinkedList.')
                }
            }
        }       
    }

    display() {
        let toDisplay = []
        let curr = this.head
        while(curr) {
            toDisplay.push(curr.val)
            curr = curr.next
        }
        return toDisplay.reverse()
    }
}

module.exports = DoublyLinkedList