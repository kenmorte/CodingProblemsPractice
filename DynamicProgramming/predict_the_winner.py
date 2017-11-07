# https://leetcode.com/problems/predict-the-winner/description/

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        self.table = [[None for n in nums] for n in nums]
        self.nums = nums
        for i in range(len(nums)):
            self.table[i][i] = (nums[i], 0)
        res = self.memo(0,len(nums)-1)
        return res[0] >= res[1]
            
    def memo(self, i, j):
        if self.table[i][j]: return self.table[i][j]
        left = self.memo(i,j-1)
        down = self.memo(i+1,j)
        
        pick_left = self.nums[i] + down[1]
        pick_right = self.nums[j] + left[1]
        
        result = (pick_left, down[0]) if max(pick_left, pick_right) == pick_left else (pick_right, left[0])
        self.table[i][j] = result
        return result
            
