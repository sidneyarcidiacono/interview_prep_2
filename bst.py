"""Implement a binary search tree using a sorted array."""


class BST(object):
    """Implement class BST to implement Binary Search Tree."""

    def __init__(self, val):
        """Initialize node value and left and right children."""
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """Specify how to print node."""
        return str(self.val)


def array_to_bst(arr):
    """Convert sorted array to BST."""
    # if the list is empty, return None, we're done
    if not arr:
        return None

    # Get the middle index
    mid_val = len(arr) // 2
    # Create our root node
    node = BST(arr[mid_val])
    node.left = array_to_bst(arr[:mid_val])
    node.right = array_to_bst(arr[mid_val + 1 :])
    return node


def post_order(node):
    """Perform our post order traversal."""
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)
