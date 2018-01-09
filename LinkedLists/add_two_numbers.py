# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, L1, L2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not L1: return L2
        if not L2: return L1
        A, B = self.validate(L1, L2)
        C, res, curr = 0, None, None
        while A and B:
            S = A.val + B.val + C
            carry, sum = S//10, S%10
            if not res: curr = res = ListNode(sum)
            else: 
                curr.next = ListNode(sum)
                curr = curr.next
            A, B, C = A.next, B.next, carry
        if C: curr.next = ListNode(C)
        return res
        
    def validate(self, L1, L2):
        C1, C2 = L1, L2
        len1, len2 = 1, 1
        while C1.next:
            len1 += 1
            C1 = C1.next
        while C2.next:
            len2 += 1
            C2 = C2.next
        for _ in xrange(max(0, len2-len1)): 
            C1.next = ListNode(0)
            C1 = C1.next
        for _ in xrange(max(0, len1-len2)): 
            C2.next = ListNode(0)
            C2 = C2.next
        return (L1, L2)
