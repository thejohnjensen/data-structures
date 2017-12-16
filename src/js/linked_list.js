'use strict'

class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class LinkedList {
    constructor(iterable = []) {
        this.head = null
        this.length = 0
        for (var i = 0; i < iterable.length; i++) {
            this.push(iterable[i]);
        }
    }

    push(val) {
        var new_node = new Node(val)
        if(this.length === 0) {
            this.head = new_node
            this.length++
        } else {
            const curr = this.head
            new_node.next = curr
            this.head = new_node
            this.length++
        }
    }

    pop() {
        if(this.length === 0) {
            throw('Your LinkedList is empty.')
        } else {
            const toReturn = this.head
            this.head = toReturn.next
            this.length--
            return toReturn.val
        }
    }

    size() {
        return this.length
    }

    search(val) {
        if(this.length === 0) {
            throw('Your LinkedList is empty.')
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
            throw('Your LinkedList is empty.')
        } else {
            let curr = this.head
            let found = false
            if(curr.val === val) {
                let toRemove = curr
                this.head = curr.next
                curr.next = null
                this.length--
                return
            }
            let prev = null
            while(!found) {
                if(curr.val === val) {
                    found = true
                    let toRemove = curr
                    prev.next = curr.next
                    curr.next = null
                    this.length--
                    return
                } else if(curr.next) {
                    prev = curr
                    curr = curr.next
                } else {
                    throw('Val not in LinkedList.')
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

module.exports = LinkedList