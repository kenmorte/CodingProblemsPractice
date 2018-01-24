# https://leetcode.com/problems/length-of-last-word/discuss/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        i = len(s)-1
        while i >= 0 and s[i] == ' ': i -= 1
        if i < 0: return 0
        cnt = 0
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
        return cnt
