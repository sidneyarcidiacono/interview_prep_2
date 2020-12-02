"""Implement a queue."""


class Queue:
    """Define class Queue."""

    def __init__(self):
        """Initialize items as a dynamic array."""
        self.items = []

    def push(self, item):
        """Push item to end of queue."""
        self.items.append(item)

    def pop(self):
        """
        Queues are First In First Out,

        So whatever was added first (first item
        in our list) must be removed first.
        """
        return self.items.pop(0)

    def peek(self):
        """Look at the front of the queue."""
        return self.items[0]
