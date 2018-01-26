# https://leetcode.com/problems/power-of-four/description/

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # O(1) time
        if num == 0: return False
        if num == 1: return True
        if num & 1 or num & 2: return False
        cnt = 0
        num = num >> 2
        while num:
            cnt += num & 1
            num = num >> 1
            if num & 1: return False
            num = num >> 1
        return cnt == 1
        
        # O(logn) time
        # copy = 1
        # while copy < num:
        #     copy *= 4
        # return copy == num
