# https://leetcode.com/problems/counting-bits/description/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = list()
        for n in range(num+1):
            result.append(self.getNumberOfOnes(n))
        return result
        
    def getNumberOfOnes(self, num):
        count = 0
        while num != 0:
            count += num & 1
            num = num >> 1
        return count
