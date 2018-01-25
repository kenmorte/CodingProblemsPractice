# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for n in xrange(left,right+1):
            if self.isSelfDividing(n): res.append(n)
        return res
    
    def isSelfDividing(self, n):
        digits = set(int(digit) for digit in str(n))
        if 0 in digits: return False
        for digit in digits:
            if n % digit: return False
        return True
