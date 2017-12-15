# https://leetcode.com/problems/array-nesting/description/

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        visited = set()
        res = 0
        for i in xrange(len(nums)):
            if i not in visited: 
                # DFS iterative
                curr = i
                length = 0
                while curr >= 0 and curr < len(nums) and curr not in visited:
                    visited.add(curr)
                    length += 1
                    curr = nums[curr]
                res = max(res, length)
        return res
