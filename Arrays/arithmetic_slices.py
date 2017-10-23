# https://leetcode.com/problems/arithmetic-slices/discuss/

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        diff = None    # Current diff for arithmetic slice
        foundConsecutive = 0   # Number of consecutive arithmetic slice elements found
        sliceLength = 1    # Current slice length
        
        for i in range(len(A) - 1):
            currentNum = A[i]
            nextNum = A[i+1]  # Look ahead from the current position
            
            currentDiff = nextNum - currentNum
            if diff is None:
                diff = currentDiff
            
            if currentDiff == diff: # Next num provides an arithmetic slice
                sliceLength += 1
                if sliceLength >= 3:
                    foundConsecutive += 1
                    result += foundConsecutive
            else:   # Next num interrupts current arithmetic slice
                diff = currentDiff
                foundConsecutive = 0
                sliceLength = 2
            
        return result
