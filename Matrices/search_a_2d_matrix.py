# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]: return False
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m-1
        while L < R:
            M = (L+R)//2
            if matrix[M][0] > target: R = M
            else: L = M+1
        
        if matrix[L][0] > target: L -= 1
            
        LH, RH = 0, n-1
        while LH < RH:
            MH = (LH+RH)//2
            if matrix[L][MH] >= target: RH = MH
            else: LH = MH+1
        
        return matrix[L][LH] == target
