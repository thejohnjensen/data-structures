'use strict'

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0
    }

    push(val) {
        var new_node = new Node(val)
        if(this.size === 0) {
            this.head = new_node
            this.size++
        } else {
            const curr = this.head
            new_node.next = curr
            this.head = new_node
            this.size++
        }
    }

    pop() {
        if(this.size === 0) {
            throw('Your LinkedList is empty.')
        } else {
            
        }
    }
}

module.exports = LinkedList