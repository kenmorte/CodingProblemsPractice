# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        if n == 1:
            return True
        
        prev_rightmost_bit = n & 1;
        n = n >> 1;
        
        while n != 0:
            rightmost_bit = n & 1;
            if rightmost_bit == prev_rightmost_bit:
                return False
            prev_rightmost_bit = rightmost_bit
            n = n >> 1;
            
        return True
