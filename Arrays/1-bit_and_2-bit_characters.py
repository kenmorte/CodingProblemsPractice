# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits:
            return False
        
        is_current_bit_zero = not bits[0]
        i = 0
        
        while i < len(bits):
            is_current_bit_zero = not bits[i]
            i += 1 if is_current_bit_zero else 2
        
        return is_current_bit_zero
