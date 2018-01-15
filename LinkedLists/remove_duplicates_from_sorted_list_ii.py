# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, H):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not H: return
        P, C, N = None, H, H.next
        while C:
            if N and C.val == N.val:
                val = C.val
                while C and C.val == val:
                    C = N
                    N = C.next if C else None
                if P: P.next = C
                else: H = C
            else:
                P = C
                C = N
                N = C.next if C else None
        return H
