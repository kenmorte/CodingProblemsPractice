# https://leetcode.com/problems/permutations/description/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return[]
        S, res = set(nums), []
        self.backtrack(S, res, [])
        return res
        
    def backtrack(self, S, res, curr):
        if not S: 
            res.append(curr)
            return
        for c in list(S):
            S.remove(c)
            self.backtrack(S, res, curr + [c])
            S.add(c)
        
