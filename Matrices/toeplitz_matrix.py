# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in xrange(len(matrix)-1,-1,-1):
            j = 0
            val = matrix[i][j]
            while i < len(matrix) and j < len(matrix[i]):
                if matrix[i][j] != val: return False
                i += 1
                j += 1
        for j in xrange(1,len(matrix[0])):
            i = 0
            val = matrix[i][j]
            while i < len(matrix) and j < len(matrix[i]):
                if matrix[i][j] != val: return False
                i += 1
                j += 1
        return True
            
