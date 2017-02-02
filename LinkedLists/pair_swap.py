# Return the head node of the singly linked list with each pair of nodes swapped. 
#   If there is a last odd node leave it in place.
# Example:    Input: 1 -> 2 -> 3 -> 4 -> 5, Output: 2 -> 1 -> 4 -> 3 -> 5 

class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next
  def __repr__(self):
    result = ""
    result += str(self.value)
    current = self.next
    while (current is not None):
      result += "->" + str(current.value)
      current = current.next
    result += "->None"
    return result

head = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6))))))
def pair_swap(head) -> Node:
  if head is None or head.next is None:
    return head
    
  prev = None
  current = head
  next = current.next
  
  while (next is not None):
    if prev is None:  # we're at the head
    
      # assign the new head to the second node
      head = next

      # move first node's next to the third node
      current.next = next.next
      
      # move second node's next to the first node (now the first node)
      head.next = current
      
      # move on to next iteration
      prev = current
      current = current.next
      
      if current is None:
        return head
        
      next = current.next
      
    else: # we're in the middle of the linked list
    
      # swap the pair
      current.next = next.next
      next.next = current
      
      # connecting previous pair to first node of current pair
      prev.next = next
      
      # move on to the next iteration
      prev = current
      current = current.next
      
      if current is None:
        return head
      
      next = current.next
      
  return head
  
print(pair_swap(head))
  
  
  
