# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, L1, L2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not L1: return L2
        if not L2: return L1
        res_head = res_curr = None
        C1, C2 = L1, L2
        while C1 and C2:
            N1, N2 = C1.next, C2.next
            if C1.val <= C2.val:
                if not res_head: res_head = res_curr = C1
                else: 
                    res_curr.next = C1
                    res_curr = res_curr.next
                C1.next = None
                C1 = N1
            else:
                if not res_head: res_head = res_curr = C2
                else: 
                    res_curr.next = C2
                    res_curr = res_curr.next
                C2.next = None
                C2 = N2
        if C1: res_curr.next = C1
        elif C2: res_curr.next = C2
        return res_head
            
                
