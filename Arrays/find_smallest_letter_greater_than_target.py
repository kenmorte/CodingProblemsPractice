# https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/110005

class Solution(object):
    def nextGreatestLetter(self, L, T):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if len(L) < 2: return ''
        A = 'abcdefghijklmnopqrstuvwxyz'
        C = A[A.index(T)+1:] + A
        for c in C:
            exists = self.binarySearch(c, L)
            if exists: return c
        return ''
    
    def binarySearch(self, c, A):
        L, R = 0, len(A)-1
        while L < R:
            M = (L+R)//2
            if c == A[M]: return True
            elif ord(c) < ord(A[M]): R = M
            else: L = M+1
        return A[L] == c
