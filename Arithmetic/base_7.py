# https://leetcode.com/problems/base-7/description/

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        isNeg = num < 0
        num = abs(num)
        res = ''
        while num:
            res += str(num%7)
            num /= 7
        return ('-' if isNeg else '') + res[::-1]
