# https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0
        isNeg = x < 0
        x = abs(x)
        y = int(x)
        factor = 1
        while y:
            factor *= 10
            y = y // 10
        factor /= 10
        # stack = []
        
        res = 0
        while x:
            # stack.append(x%10)
            digit = x%10
            res += digit * factor
            factor /= 10
            x = x//10
        '''
        factor, res = 1, 0
        while stack:
            res += stack.pop() * factor
            factor *= 10
        '''
        if res > (2**31)-1: return 0
        return (-1 if isNeg else 1) * res
