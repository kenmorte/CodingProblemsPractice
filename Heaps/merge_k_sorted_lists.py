# https://leetcode.com/problems/merge-k-sorted-lists/description/

import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, KL):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not KL: return []
        P, H, res, curr = [L for L in KL], [], None, None
        for i,L in enumerate(KL): heapq.heappush(H, (L.val,i) if L else (float('inf'),i))
        while H[0][0] != float('inf'):
            v, Li = heapq.heappop(H)
            if not res: curr = res = P[Li]
            else: 
                curr.next = P[Li]
                curr = curr.next
            P[Li] = P[Li].next
            heapq.heappush(H, (float('inf') if not P[Li] else P[Li].val, Li))
        return res
            
