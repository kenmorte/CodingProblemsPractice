# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        res = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s) and s[i] not in 'aeiouAEIOU':
                i += 1
            if i == len(s): return ''.join(res)
            
            while j >= 0 and s[j] not in 'aeiouAEIOU':
                j -= 1
            if j == -1: return ''.join(res)
            
            if j <= i: return ''.join(res)
            
            temp = s[i]
            res[i] = s[j]
            res[j] = temp
            i, j = i+1,j-1
        return ''.join(res)
