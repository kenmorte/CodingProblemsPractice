# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution(object):
    def searchMatrix(self, m, v):
        if not m or not m[0]: return False
        r, c = 0, len(m[0])-1
        while r < len(m) and c >= 0:
            if m[r][c] == v: return True
            elif m[r][c] < v: r += 1
            elif m[r][c] > v: c -= 1
        return False
    
    def searchMatrix1(self, m, v):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not m: return False
        L, R = 0, len(m[0])-1
        T, B = 0, len(m)-1
        while L < R and T < B:
            if self.bsh(m[T], L, R, v) or self.bsv(m, T, B, L, v):
                return True
            L += 1
            T += 1
        if T == B: return self.bsh(m[T], L, R, v)
        return self.bsv(m, T, B, L, v)
        
    def bsh(self, a, L, R, v):
        if L > R: return False
        if L < 0 or R >= len(a): return False
        if a[L] > v: return False
        while L < R:
            M = (L+R) // 2
            if a[M] < v: L = M + 1
            elif a[M] > v: R = M
            else: return True
        return a[L] == v
    
    def bsv(self, a, T, B, L, v):
        if T > B: return False
        if T < 0 or B >= len(a): return False
        if L < 0 or L >= len(a[T]): return False
        if a[T][L] > v: return False
        while T < B:
            M = (T+B) // 2
            if a[M][L] < v: T = M + 1
            elif a[M][L] > v: B = M
            else: return True
        return a[T][L] == v
