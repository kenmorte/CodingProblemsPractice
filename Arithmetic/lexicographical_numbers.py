# https://leetcode.com/problems/lexicographical-numbers/description/

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0: return []
        res = []
        for cn in [1,2,3,4,5,6,7,8,9]:
            if cn <= n: res += [cn]
            self.dfs(cn*10, n, res)
        return res
            
    def dfs(self, cn, n, res):
        for i in [0,1,2,3,4,5,6,7,8,9]:
            if cn+i > n: return
            res += [cn+i]
            self.dfs((cn+i)*10, n, res)
            
