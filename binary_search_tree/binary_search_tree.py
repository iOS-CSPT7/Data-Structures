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
import sys 
sys.path.append('../stack')
from lambdastack import Stack 
sys.path.append('../queue')
from lambdaqueue import Queue 
print(type(sys.path))

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self 
        done = False 
        while not done:
            if value >= current_node.value:
                if not current_node.right == None:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(value)
                    done = True 
            elif value < current_node.value: 
                if not current_node.left == None:
                    current_node = current_node.left 
                else: 
                    current_node.left = BSTNode(value)
                    done = True 
        # if value < self.value:
        #     if self.left == None: 
        #         self.left = BSTNode(value)
        #     else: 
        #         self.left.insert(value)
        # if value >= self.value: 
        #     if self.right == None: 
        #         self.right = BSTNode(value)
        #     else: 
        #         self.right.insert(value)
        
        # Tim's solution
        # if value >= self.value:
        #     if self.right is not None:
        #         self.right.insert(value)
        #     else:
        #         new_node: BSTNode(value)
        #         self.right = new_node
        # else: 
        #     if self.left is not None:
        #         self.left.insert(value)
        #     else: 
        #         new_node = BSTNode(value)
        #         self.left = new_node 


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

        # Tim's solution 
        # if self.value == target:
        #     return True 
        # elif target > self.value: 
        #     if self.right is not None: 
        #         return self.right.contains(target)
        #     else: 
        #         return False 
        # else: 
        #     if self.left is not None:
        #         return self.left.contains(target) #making it do its own work with recursion to check with the first if statement 
        #     else: 
        #         return False 
        
        

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right 
        return current_node.value 
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        if self.left:
            self.left.for_each(fn)

        fn(self.value)

        if self.right: 
            self.right.for_each(fn)

        
        
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        
        print(node.value)

        if self.right:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        new_queue = Queue()
        # make a queue 
        # enqueue the node 
        new_queue.enqueue(node)
        # as long as the queue is not empty
        while len(new_queue) != 0:
            current_node = new_queue.dequeue()
            if current_node.left:
                new_queue.enqueue(current_node.left)
            if current_node.right:
                new_queue.enqueue(current_node.right)
            new_queue.dequeue(node)
        # dequeue from the front of the queue ,this is our current node 
        # enqueue the kids of the current node on the queue 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        # make a stack 
        new_stack = Stack()
        # push the node on the stack 
        new_stack.push(node)
        # as long as the stack is not empty 
        while len(new_stack) != 0:
        # # pop off the stack, this is our current node  
            current_node = new_stack.pop()
            if current_node.left:
                new_stack.push(node.left)
            if current_node.right:
                new_stack.push(node.right)

        # #put the kids of the current node on the stack
        # check that they are not none, then put them on the stack 


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        
        if node: 
            print(node.value)

            self.pre_order_dft(node.left)

            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        
        if node: 
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
