# https://leetcode.com/problems/matchsticks-to-square/description/

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        s = sum(nums)
        if s % 4: return False
        target = s // 4
        visited = set()
        nums.sort(reverse=True)
        return (self.dfs(nums, visited, 0, 0, target) and 
                self.dfs(nums, visited, 0, 0, target) and 
                self.dfs(nums, visited, 0, 0, target) and 
                self.dfs(nums, visited, 0, 0, target))
    
    def dfs(self, nums, visited, curr, start, target):
        if curr == target: return True
        if curr > target or start >= len(nums): return False
        for i in xrange(start, len(nums)):
            if i not in visited:
                visited.add(i)
                if self.dfs(nums, visited, curr + nums[i], i+1, target): return True
                visited.remove(i)
        return False
        
                
