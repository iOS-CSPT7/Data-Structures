"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

my_node = ListNode(12)
# my_node.value = 12
# my_node.prev = None
# my_node.next = None -->(ListNode (25))
my_node.insert_after(25)
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
# efficient
#delete
#update
# removing/ adding from beginning and end 


#not to efficient: finding a value, verifying 
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #wrap the given value in a ListNode
        new_node = ListNode(value)
        self.length += 1
         #handle if list has no head
        if self.head:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        else: 
            self.head = new_node
            self.tail = self.head
            # Tim says self.tail = new_node

        #handle if list has a head
       
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value 
        # pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        else: 
            self.tail = new_node
            self.head = new_node 
        pass


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value 
        # self.delete(self.tail)
        # return value 
        # if 0 nodes
        if not self.tail: 
            return
        # if head and tail are the same (1 node)
        elif self.head == self.tail: 
            self.head = None
            self.tail = None 

        
        # if more than 1 node
        else: 
            self.tail = self.tail.prev 
            self.tail.next = None 

        self.length -= 1

        return value 


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # self.delete(node)
        # node.next = self.head
        # self.head.prev = node
        # self.head = node
   
        if node is self.head:
            return 
        value = node.value 
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail: 
            return 
        value = node.value 
        self.delete(node)
        self.add_to_tail(value)
        # pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        

        # if list is empty
        if not self.head: 
            print("You got nothing on me")
            return
        # if node is head
        self.length -= 1

        if self.head == self.tail: 
            self.head = None
            self.tail = None 
        #we have at least 2 nodes, and the node we want to delete is the head
        if node == self.head: 
            self.head = node.next 
            self.head.prev = None 

         #we have at least 2 nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None 

        else: 
            # if somewhere in the middle
            node.delete()

        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # walk through the entire list
        # keep track of the biggest value we've found 


        highest_value = self.head.value
        current_node = self.head 

        while current_node is not None:
            
            if current_node.value > highest_value:
                highest_value = current_node.value
            current_node = current_node.next 
            
        return highest_value
         # value = self.head.value 
        # current = self.head

        # while current is not None:
        #     if current.value > value:
        #         value = current.value 
        #     current = current.next
        # return value 
            
#     # iterating over lists 
#     def iterate_list(node):
#         while node is not None:
#             print(node.value)
#             node = node.next 
    


#     iterate_list(my_node)
       
    def find_middle(self):
        middle = self.head 
        end = self.head 

        while end != None and end.next.next != None: 
            end = end.next.next
            middle = middle.next 
             
        
        print(middle)
        return middle 
  
    def reverse_list(self):
        pass
    # head should be tail
    # tail should be head 
    # no recursion, no other data structures 

dll = DoublyLinkedList()
dll.add_to_tail(1)
dll.add_to_tail(2)
dll.add_to_tail(3)
dll.add_to_tail(4)
dll.add_to_tail(5)
dll.add_to_tail(6)

middle = dll.find_middle()

print(middle.value, middle.value == 3)