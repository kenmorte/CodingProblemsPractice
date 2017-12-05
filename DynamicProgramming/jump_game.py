# https://leetcode.com/problems/jump-game/description/

class Solution(object):
    def canJump(self, nums):
        if not nums: return False
        if len(nums) == 1: return True
        g = len(nums)-1
        for i in xrange(len(nums)-1, -1, -1):
            if i + nums[i] >= g: 
                g = i
        return not g
    
    def canJumpFirstSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        if len(nums) == 1: return True
        if not nums[0]: return False
        T = [False for _ in nums]
        T[-1] = True
        
        for i in xrange(len(nums)-2, -1, -1):
            j = i+1
            while j < i+1+min(nums[i],len(nums)-i-1):
                if T[j]:
                    T[i] = True
                    break
                else:
                    j += nums[j]+1
            
            # T[i] = any(T[i+1:i+1+min(nums[i],len(nums)-i-1)])
        
        return T[0]
        
    def dfs(self, i, a ,T):
        if T[i] is not None: return T[i]
        for n in xrange(1, min(a[i], len(a)-i-1)+1):
            if self.dfs(i+n, a, T):
                T[i] = True
                return True
        T[i] = False
        return False
            
            
