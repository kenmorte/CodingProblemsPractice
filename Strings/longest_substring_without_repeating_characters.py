# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        res = 0
        i = j = 0
        seen = {}
        while j < len(s):
            if s[j] not in seen: seen[s[j]] = j
            else:
                # print 'considering ', s[i:j]
                res = max(res, j-i)
                while s[j] in seen:
                    del seen[s[i]]
                    i += 1
                seen[s[j]] = j
            j += 1
        res = max(res, j-i)
        return res
