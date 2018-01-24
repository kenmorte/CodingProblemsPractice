# https://leetcode.com/problems/pascals-triangle-ii/discuss/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        res = [1]
        prevRow = self.getRow(rowIndex-1)
        for i in xrange(len(prevRow)-1): res += [prevRow[i]+prevRow[i+1]]
        res += [1]
        return res
        
