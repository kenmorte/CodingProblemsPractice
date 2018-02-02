# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        if head and not head.next: return
        mid = self.getMidNode(head)
        L, R = head, self.reverse(mid)
        changeLeft = True
        while L != R:
            if changeLeft: 
                next = L.next
                L.next = R
                L = next
            else: 
                next = R.next
                R.next = L
                R = next
            changeLeft = not changeLeft
        L.next = None
        
    def getMidNode(self, head):
        curr = head
        fast = head.next
        while fast:
            fast = fast.next
            if fast: fast = fast.next
            curr = curr.next
        return curr
    
    def reverse(self, head):
        if not head: return
        curr = head
        next = head.next
        while next:
            nextnext = next.next
            next.next = curr
            curr = next
            next = nextnext
        return curr
