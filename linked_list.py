"""Implement our linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
        new_node.next = None

    def find(self, item):
        current = self.head
        while current.data[0] != item:
            current = current.next
        if current.data[0] == item:
            return current
