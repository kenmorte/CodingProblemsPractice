# https://leetcode.com/problems/increasing-triplet-subsequence/description/

class Solution(object):
    def increasingTriplet(self, n):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(n) < 3: return False
        i,j,k = 0,1,2
        max_i,max_j,max_k = len(n)-3,len(n)-2,len(n)-1
        while i < max_i or j < max_j or k < max_k:
            i_n, j_n, k_n = min(i+1,max_i), min(j+1,max_j), min(k+1,max_k)
            if n[i] >= n[k]: 
                if n[i] < n[j]: 
                    if k == max_k:
                        if j == max_j: i = i_n
                        else: j = j_n
                    else: k = k_n
                else: i,j,k = i_n,j_n,k_n
            elif n[i] >= n[j]:
                if j == max_j: i = i_n
                elif j == k-1: j,k = j_n,k_n
                else: j = j_n
            elif n[j] >= n[k]: 
                if k == max_k: # Can't advance k any further
                    if j == max_j: i = i_n  # Can't advance j any further, so advance i
                    else: j = j_n  # Advance j
                else: k = k_n
            else: return True
        return n[i] < n[j] and n[j] < n[k]
