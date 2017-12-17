# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, A, T):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not A: return 0
        if len(A) == 1: return 0 if A[0] == T else 1
        if T not in A: return len(A)
        i, j = 0, len(A)-1
        while i < j:
            while i < j and A[i] != T: i += 1
            while i < j and A[j] == T: j -= 1
            if i == j: return i
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        return i
