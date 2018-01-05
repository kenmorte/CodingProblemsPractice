# Asked by Google 12/20/2017
# https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0: return []
        
        def dfs(p, n, L, R, s):
            if L > n: return
            if L < R: return
            if L == R and L == n: return s.add(p)
            dfs(p + '(', n, L + 1, R, s)
            dfs(p + ')', n, L, R + 1, s)
        
        s = set()
        dfs('(',n,1,0,s)
        return list(s)
