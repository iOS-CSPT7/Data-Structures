"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

   O(logn) for binary
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self == None:
            self = BSTNode(value)
        else:
            current_node = self 
            done = False 
            while not done:
                if current_node.value >= value:
                    if not current_node.right == None:
                        current_node = current_node.right
                    else:
                        current_node.right = BSTNode(value)
                        done = True 
                elif current_node.value < value: 
                    if not current_node.left == None:
                        current_node = current_node.left 
                    else: 
                        current_node.left = BSTNode(value)
                        done = True 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node  = self 
        while current_node: 
            if target == current_node.value: 
                return True
            elif target < current_node.value:
                current_node = current_node.left 
            else:
                current_node = current_node.right 
        return False 

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right 
        return current_node.value 

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
