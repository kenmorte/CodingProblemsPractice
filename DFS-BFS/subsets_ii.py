# https://leetcode.com/problems/subsets-ii/description/

from collections import Counter

class FrozenCounter(Counter):
    def __hash__(self):
        _hash = 0
        for pair in self.items():
            _hash ^= hash(pair)
        return _hash


class Solution(object):
    def subsetsWithDup(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not A: return []
        res = set()
        res.add(FrozenCounter())
        self.backtrack(A, res, [])
        return [self.counterToList(C) for C in res]
    
    def backtrack(self, A, res, curr):
        if not A: return
        curr.append(A[0])
        res.add(FrozenCounter(curr))
        self.backtrack(A[1:], res, curr)
        curr.pop()
        self.backtrack(A[1:], res, curr)
        
    def counterToList(self, C):
        res = []
        for n in C:
            res += [n]*C[n]
        return res
