"""Implement our stack."""


class Stack:
    """Define our Stack class."""

    def __init__(self):
        """Initialize items (we'll use a Python list)."""
        self.items = []

    def push(self, item):
        """
        Push item to top of stack.

        For this example, we're calling the
        end of the list the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop item from stack.

        Stacks are First In Last Out, so we'll be
        popping also from the end of the list.
        """
        return self.items.pop()

    def peek(self):
        """
        Look at the top of the stack.

        This will be the last element in
        the list.
        """
        return self.items[-1]
