https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root: return [None for i in range(k)]
        curr = root
        n = 0
        while curr:
            n += 1
            curr = curr.next
        
        orig_k = k
        k = min(k,n)
        b = [0 for i in range(k)]
        r = [None for i in range(k)]
        for i in range(k): b[i] = (n//k) + 1 if i < n % k else n // k
        curr = root
        for i,bucket in enumerate(b):
            r_curr = r[i]
            while bucket > 0:
                if not r_curr: r[i] = r_curr = ListNode(curr.val)
                else:
                    r_curr.next = ListNode(curr.val)
                    r_curr = r_curr.next
                curr = curr.next
                bucket -= 1
        if orig_k > n: r += [None for i in range(orig_k - n)]
        return r
