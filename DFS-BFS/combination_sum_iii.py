https://leetcode.com/problems/combination-sum-iii/description/

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k <= 0 or n <= 0: return []
        res = set()
        for i in range(1,10):
            self.dfs(n-i,{i},k-1,res)
        return [list(s) for s in res]
        
    def dfs(self, n, c, k, res):
        if n < 0: return
        if k == 0: return res.add(frozenset(c))
        if k == 1:
            if n not in c and n > 0 and n < 10:
                c.add(n)
                res.add(frozenset(c))
                c.remove(n)
            return
        for i in range(1,10):
            if i not in c:
                c.add(i)
                self.dfs(n-i,c,k-1,res)
                c.remove(i)
