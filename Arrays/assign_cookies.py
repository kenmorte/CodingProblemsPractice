# https://leetcode.com/problems/assign-cookies/description/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s: return 0
        
        g.sort()
        s.sort()
        
        g_i = 0
        result = 0
        for size in s:
            if size >= g[g_i]:
                result += 1
                g_i += 1
                if g_i >= len(g): break
        return result
