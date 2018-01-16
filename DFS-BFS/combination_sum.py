# https://leetcode.com/problems/combination-sum/description/

class Solution(object):
    def combinationSum(self, S, T):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not S or T <= 0: return []
        res = []
        self.dfs(S, 0, T, [], res)
        return res
    
    def dfs(self, S, sum, T, curr, res):
        if sum > T: return
        if sum == T:
            res.append(list(curr))
            return
        if not S: return
        curr.append(S[0])
        self.dfs(S, sum + S[0], T, curr, res)
        curr.pop()
        self.dfs(S[1:], sum, T, curr, res)
