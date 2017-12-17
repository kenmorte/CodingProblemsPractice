# https://leetcode.com/problems/house-robber-ii/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        return max(self.robHouses(nums[:len(nums)-1]), self.robHouses(nums[1:]))
            
    def robHouses(self, nums):
        dp = [n for n in nums]
        dp[1] = max(dp[0], dp[1])
        for i in xrange(2,len(nums)): dp[i] = max(dp[i] + dp[i-2], dp[i-1])
        return dp[-1]
