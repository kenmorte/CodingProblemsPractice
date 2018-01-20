# https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = secondLargest = thirdLargest = float('-inf')
        for n in nums:
            if n == largest or n == secondLargest or n == thirdLargest: continue
            if n > largest:
                thirdLargest = secondLargest
                secondLargest = largest
                largest = n
            elif n > secondLargest:
                thirdLargest = secondLargest
                secondLargest = n
            elif n > thirdLargest:
                thirdLargest = n
        return thirdLargest if thirdLargest != float('-inf') else largest
