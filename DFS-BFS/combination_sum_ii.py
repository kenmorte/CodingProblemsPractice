# https://leetcode.com/problems/combination-sum-ii/description/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        self.dfs(candidates, [], res, 0, target)
        return list(res)
    
    def dfs(self, arr, comb, res, sum, k):
        if sum == k: 
            res.add(tuple(sorted(comb)))
            return
        if not arr or sum > k: return
        comb.append(arr[0])
        self.dfs(arr[1:], comb, res, sum + arr[0], k)
        comb.pop()
        self.dfs(arr[1:], comb, res, sum, k)
