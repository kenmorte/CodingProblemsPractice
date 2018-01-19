# https://leetcode.com/problems/find-anagram-mappings/description/

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        Bmap = {}
        res = []
        for i,b in enumerate(B): Bmap[b] = i
        for i in xrange(len(A)): res += [Bmap[A[i]]]
        return res
