# https://leetcode.com/problems/add-digits/#/description

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        result = num # just some random non-one-digit number here
        
        while len(str(result)) > 1:
            digits = [int(c) for c in str(result)]
            result = sum(digits)
            
        return result
