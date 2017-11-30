# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution(object):
    def search(self, a, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not a: return -1
        L, R = 0, len(a)-1
        while L != R:
            M = (L+R)//2
            if t == a[M]: return M
            if self.inRange(a[L], a[M], t): R = M
            elif self.inRange(a[M], a[R], t): L = M+1
            else: return -1
        return L if a[L] == t else -1
    
    def inRange(self, L, R, v):
        if L < R: return v >= L and v <= R
        elif L > R: return v >= L or v <= R
        else: return v == L
        
