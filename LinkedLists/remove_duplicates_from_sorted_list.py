# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        curr, next = head, head.next
        while next:
            while next and next.val == curr.val: next = next.next
            if not next: break
            curr.next = next
            curr = curr.next
            next = curr.next
        curr.next = next
        return head
