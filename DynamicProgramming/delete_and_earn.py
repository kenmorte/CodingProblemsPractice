# Asked by Quip on 1/4/2018
# https://leetcode.com/problems/delete-and-earn/description/

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        buckets = [0 for _ in xrange(max(nums)+1)]
        for num in nums: buckets[num] += 1
        dp = [n*i for i,n in enumerate(buckets)]
        for i in xrange(2,len(dp)): dp[i] = max(dp[i-1],dp[i-2]+dp[i])
        return dp[-1]
        
