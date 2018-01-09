# https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not A: return []
        res = [[]]
        self.backtrack(A, res, [])
        return res
    
    def backtrack(self, A, res, curr):
        if not A: return
        curr.append(A[0])
        res.append(list(curr))
        self.backtrack(A[1:], res, curr)
        curr.pop()
        self.backtrack(A[1:], res, curr)
