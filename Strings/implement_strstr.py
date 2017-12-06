# https://leetcode.com/problems/implement-strstr/description/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle: return 0
        if haystack and not needle: return 0
        if len(needle) > len(haystack): return -1
        for i in xrange(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1
