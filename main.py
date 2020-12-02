"""Import modules."""
from stack import Stack
from queue import Queue
from hash_table import HashTable
from bst import array_to_bst, post_order

# 1. Create a stack using a dynmaic array. Implement the push(), pop(), and peek() methods and discuss the time complexity of this implementation in your video walkthrough
print("----------------------------------------------")
print("------STACK------")
print("----------------------------------------------")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Original stack items: {stack.items}")
print(f"Original stack peek: {stack.peek()}")
print(f"Popped item: {stack.pop()}")
print(f"Peek after popping: {stack.peek()}")

print("----------------------------------------------")
print("------QUEUE------")
print("----------------------------------------------")


# 2. Create a queue using a dynmaic array. Implement the push(), pop(), and peek() methods and discuss the time complexity of this implementation in your video walkthrough

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(f"Original queue items: {queue.items}")
print(f"Original queue peek: {queue.peek()}")
print(f"Popped item: {queue.pop()}")
print(f"Peek after popping: {queue.peek()}")

# 3. In your video discuss how a hash table works. What data structures do you use to build one? How do you handle collisions? What makes a hash table effective at quickly looking up items?

print("----------------------------------------------")
print("------HASH TABLE------")
print("----------------------------------------------")


hash_table = HashTable(10)

hash_table.insert(("Sid", 23))
print(hash_table.lookup("Sid"))

# 4. Assume you are given a valid binary search tree, write pseudocode (final code solution optional) to perform a recursive post-order traversal of the tree

# Assuming that we're given a valid bst, the post-order traversal would look something like this:


bst = array_to_bst([1, 2, 3, 4, 10, 12, 20])
post_order(bst)
