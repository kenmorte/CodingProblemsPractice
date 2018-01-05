# https://leetcode.com/problems/increasing-subsequences/description/

class Solution(object):
    def findSubsequences(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not A: return []
        res = set()
        self.dfs(A, [], res, float('-inf'))
        return [list(subseq) for subseq in res]
    
    def dfs(self, A, curr, res, min):
        if not A:
            if len(curr) >= 2: res.add(tuple(curr))
            return
        if A[0] < min: self.dfs(A[1:], curr, res, min)
        else:
            curr.append(A[0])
            self.dfs(A[1:], curr, res, A[0])
            curr.pop()
            self.dfs(A[1:], curr, res, min)
