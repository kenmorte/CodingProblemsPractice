# https://leetcode.com/problems/relative-ranks/description/

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = ['' for _ in nums]
        rank = 1
        for i,n in sorted([(i,nums[i]) for i in xrange(len(nums))], key=lambda t: t[1], reverse=True):
            res[i] = 'Gold Medal' if rank == 1 else 'Silver Medal' if rank == 2 else 'Bronze Medal' if rank == 3 else str(rank)
            rank += 1
        return res
