# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: return []
        t = self.allPalindromes(s)
        res, curr = [], []
        self.dfs(s[1:], s[0], curr, res, t)
        return res
    
    def dfs(self, s, p, curr, res, t):
        if not s:
            if p in t: res.append(curr+[p])
            return
        if p in t: self.dfs(s[1:], s[0], curr+[p], res, t)
        self.dfs(s[1:], p+s[0], curr, res, t)
        
    def allPalindromes(self, s):
        t = set()
        for i in xrange(len(s)):
            L, R = i, i
            
            while L >= 0 and R < len(s) and s[L] == s[R]:
                t.add(s[L:R+1])
                L, R = L-1, R+1
            
            L,R = i-1, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                t.add(s[L:R+1])
                L, R = L-1, R+1
        return t
