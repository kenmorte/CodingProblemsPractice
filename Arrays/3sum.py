# https://leetcode.com/problems/3sum/description/

from collections import Counter

class Solution(object):
    def threeSum(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(A) < 3: return []
        res = set()
        for i in xrange(len(A)-2):
            for pair in self.twoSum(A[i+1:], -A[i]):
                if not self.isTripletInSet((A[i], pair[0], pair[1]), res):
                    res.add((A[i], pair[0], pair[1]))
        return [list(T) for T in res]
    
    def twoSum(self, A, k):
        if len(A) < 2: return set()
        C = Counter(A)
        res = set()
        for n in A:
            if k-n == n and C[n] > 1: res.add((n,n))
            elif k-n != n and k-n in C and (n,k-n) not in res and (k-n,n) not in res: res.add((n,k-n))
        return res
    
    def isTripletInSet(self, T, S):
        a, b, c = T
        for triplet in [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,b,a),(c,a,b)]:
            if triplet in S: return True
        return False
