# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        if head and not head.next: return True
        
        length = 0
        curr = head
        
        # Calculate the length
        while curr:
            length += 1
            curr = curr.next
            
        # Iterate halfway through the linked list
        curr, prev = head, None
        for i in xrange(length//2):
            prev = curr
            curr = curr.next
            
        # Reverse the second half of the linked list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Check palindrome from both sides of linked list
        curr, rhead = head, prev
        for i in xrange(length//2):
            if curr.val != rhead.val: return False
            curr, rhead = curr.next, rhead.next
        return True
