# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return None
        if n <= 0: return head
        fast = slow = head
        for _ in xrange(n): fast = fast.next
        if not fast: return head.next
        while fast.next: slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head
