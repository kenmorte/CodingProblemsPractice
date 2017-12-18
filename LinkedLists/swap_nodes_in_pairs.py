# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head
        next = head.next
        next_next = next.next
        next.next = head
        head.next = self.swapPairs(next_next)
        return next
