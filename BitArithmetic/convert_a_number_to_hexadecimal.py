# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        if num < 0: num &= ((1 << 32) - 1)
        hex = {n:str(n) for n in xrange(10)}
        hex.update({10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'})
        res = ''
        while num:
            res += hex[num & 15]
            num = num >> 4
        return res[::-1]
