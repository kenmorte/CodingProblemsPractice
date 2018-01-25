# https://leetcode.com/problems/pour-water/description/

class Solution(object):
    def pourWater(self, heights, V, k):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if not V: return heights
        H = list(heights)
        for _ in xrange(V):
            leftMinIndex, rightMinIndex = k, k
            for i in xrange(k-1,-1,-1):
                if H[i] > H[leftMinIndex]: break
                if H[i] < H[leftMinIndex]: leftMinIndex = i
            for i in xrange(k+1,len(H)):
                if H[i] > H[rightMinIndex]: break
                if H[i] < H[rightMinIndex]: rightMinIndex = i
            minHeight = min(H[leftMinIndex], H[rightMinIndex], H[k])
            if H[k] == minHeight: H[k] += 1
            elif H[leftMinIndex] < H[k]: H[leftMinIndex] += 1
            else: H[rightMinIndex] += 1
        return H
