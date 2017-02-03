"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# Keep a fast and a slow pointer
#   Fast pointer advances by two nodes
#   Slow pointer advances by one node
# If fast catches up to the slow at any point --> we have a cycle!
# Else  --> we don't have a cycle 

def has_cycle(head):
    
    # No linkedlist = no cycle
    if head is None:
        return False
    
    fast = slow = head
    while fast is not None:
        
        # Slow/fast pointer reached the end of the linked list
        if slow.next is None or fast.next is None:
            return False
        
        # Advance the slow and fast pointers
        slow = slow.next
        fast = fast.next.next
        
        # If the fast pointer caught up to the slow one --> cycle detected
        if slow == fast:
            return True
        
    
    # Fast reached the end of the linked list, no cycle detected
    return False
    
