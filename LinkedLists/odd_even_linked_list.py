# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        HO = CO = None
        HE = CE = None
        curr = head
        i = 1
        while curr:
            next = curr.next
            curr.next = None
            if i % 2 == 0:
                if not HE: HE = CE = curr
                else:
                    CE.next = curr
                    CE = CE.next
            else: # odd
                if not HO: HO = CO = curr
                else:
                    CO.next = curr
                    CO = CO.next
            curr = next
            i += 1
        if not CO: return HE
        CO.next = HE
        return HO
