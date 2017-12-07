# https://leetcode.com/problems/add-two-numbers-ii/description/

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
        
        S1, S2 = [],[]
        curr1, curr2 = L1, L2
        
        while curr1:
            S1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            S2.append(curr2.val)
            curr2 = curr2.next
        
        res, c = None, 0
        while S1 or S2:
            if S1 and S2:
                x, y = S1.pop(), S2.pop()
                c, r = self.getCR(x+y+c)
                if not res: res = ListNode(r)
                else:
                    curr = ListNode(r)
                    curr.next = res
                    res = curr
            else:
                S = S1 if S1 else S2
                x = S.pop()
                c, r = self.getCR(x+c)
                curr = ListNode(r)
                curr.next = res
                res = curr
        if c:
            curr = ListNode(c)
            curr.next = res
            res = curr
        return res
        
    def getCR(self, num):
        num = str(num)
        n = len(num)
        c, r = num[:n-1], int(num[-1])
        c = 0 if not c else int(c)
        return (c,r)
