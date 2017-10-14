# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = dict()
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = len(s)
        for i in range(len(letters)):
            values[letters[i]] = i + 1
        result = 0
        
        for c in s:
            result += values[c] * (26 ** (n - 1))
            n -= 1
            
        return result
        
