# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

import functools

class Solution(object):
    def maxSumOfThreeSubarrays(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        subarrsum = self.getSubarraySums(A, k)
        dp1 = [None for _ in subarrsum]
        dp2 = list(dp1)
        dp3 = list(dp2)
        
        # Base case
        dp1[0] = (subarrsum[0], 0)
        dp2[0] = (subarrsum[0], 0, 0)
        dp3[0] = (subarrsum[0], 0, 0, 0)
        
        def lexiComp(t1, t2): 
            for i in range(3):
                if t1[i] != t2[i]: return t1[i] - t2[i]
            return t1[0] - t2[0]
        
        # Fill all max of 1 subarrays
        for i in xrange(1, len(dp1)):
            prev, index = dp1[i-1]
            dp1[i] = max(dp1[i-1], (subarrsum[i],i), key=lambda t:t[0])
            
        # Fill all max of 2 subarrays
        for i in xrange(1,len(dp2)):
            if i < k:
                dp2[i] = max(dp2[i-1], (subarrsum[i], 0, i), key=functools.cmp_to_key(lexiComp))
                continue
            prev, prev_index = dp1[i-k]
            dp2[i] = max(dp2[i-1], (prev + subarrsum[i], prev_index, i), key=functools.cmp_to_key(lexiComp))
            
        # Fill all max of 3 subarrays
        kTimes2 = 2*k
        for i in xrange(1,len(dp3)):
            if i < kTimes2:
                dp3[i] = max(dp3[i-1], (subarrsum[i], 0, 0, i), key=functools.cmp_to_key(lexiComp))
                continue
            prev, i1, i2 = dp2[i-k]
            dp3[i] = max(dp3[i-1], (prev + subarrsum[i], i1, i2, i), key=functools.cmp_to_key(lexiComp))
        
        return dp3[-1][1:]
        
    def getSubarraySums(self, A, k):
        curr = sum(A[:k])
        ptr = 0
        res = [curr]
        for n in A[k:]:
            curr = curr - A[ptr] + n
            ptr += 1
            res.append(curr)
        return res
