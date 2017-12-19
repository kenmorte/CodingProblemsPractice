# https://leetcode.com/problems/search-insert-position/description/

class Solution(object):
    def searchInsert(self, A, T):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not A: return 0
        L, R = 0, len(A)-1
        while L < R:
            M = (L+R)//2
            if T == A[M]: return M
            elif T < A[M]: R = M
            else: L = M+1
        if A[L] < T: return L+1
        return L
