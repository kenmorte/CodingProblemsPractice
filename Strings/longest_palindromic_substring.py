# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        res = ''
        for i in xrange(len(s)):
            # Look for longest odd palindrome here 
            L,R = i,i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            res = max(res, s[L+1:R], key=len)
            
            # Look for longest even palindrome here
            L,R = i,i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            res = max(res, s[L+1:R], key=len)
        return res
