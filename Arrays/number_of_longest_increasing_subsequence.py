# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        dp = [1 for _ in nums]
        counts = [1 for _ in nums]
        for i in xrange(len(nums)-2,-1,-1):
            longest = dp[i]
            
            for j in xrange(i+1, len(nums)):
                if nums[j] > nums[i]:                    
                    if 1+dp[j] > longest:
                        longest = 1+dp[j]
                        counts[i] = counts[j]
                    elif 1+dp[j] == longest:
                        counts[i] += counts[j]
            
            dp[i] = longest
        
        longest = 0
        cnt = 0
        for i, lis in enumerate(dp):
            if lis > longest:
                longest = lis
                cnt = counts[i]
            elif lis == longest:
                cnt += counts[i]
        return cnt
                    
            
            
                    
