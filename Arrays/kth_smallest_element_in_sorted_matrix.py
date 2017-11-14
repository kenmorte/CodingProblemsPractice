# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution(object):
    def kthSmallest(self, m, k):
        l = sorted([n for r in m for n in r])
        return l[k-1]
    
    def kthSmallest1(self, m, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not m: return None
        ptrs = [0 for _ in m]
        res = None
        while k > 0:
            c_m, c_i = float('inf'), -1
            for i,j in enumerate(ptrs):
                if j >= len(m[i]): continue
                if m[i][j] < c_m: c_m,c_i = m[i][j],i
            ptrs[c_i] += 1
            k -= 1
            res = c_m
        return res
