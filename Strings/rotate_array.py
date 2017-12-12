# https://leetcode.com/problems/rotate-array/description/

from collections import deque

class Solution(object):
    # O(n) time
    # O(1) space
    def rotate(self, nums, k):
        if len(nums) <= 1: return
        
        n = len(nums)
        k = (-1 if k < 0 else 1)*(abs(k) % n)
        if not k: return
        
        # Swap k values from edges
        for i in xrange(min(abs(k),len(nums)//2)):
            j = len(nums)-1-i
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        partitionIndex = k if k > 0 else len(nums)+k
        numberOfInPlaceElems = max(0, len(nums)-(2*abs(k)))
        
        if k > 0:
            nums[:partitionIndex] = nums[:partitionIndex][::-1]
            nums[partitionIndex+numberOfInPlaceElems:] = nums[partitionIndex+numberOfInPlaceElems:][::-1]
            
            for i in xrange(partitionIndex+numberOfInPlaceElems, len(nums)):
                j = i-1
                for _ in xrange(numberOfInPlaceElems):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i -= 1
                    j -= 1
                    if j < 0: break
        else:
            nums[partitionIndex:] = nums[partitionIndex:][::-1]
            nums[:abs(k)] = nums[:abs(k)][::-1]
            
            for i in xrange(abs(k)-1,-1,-1):
                j = i+1
                for _ in xrange(numberOfInPlaceElems):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i += 1
                    j += 1
                    if j >= len(nums): break
        
    
    def rotateFirstSolution(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # O(n) time, O(n) space
        if len(nums) <= 1: return
        
        n = len(nums)
        k = (-1 if k < 0 else 1)*(abs(k) % n)
        if not k: return
        
        DQ1 = deque()
        DQ2 = deque()
        
        for i in xrange(0,k,-1 if k<0 else 1):
            index = len(nums)-1-i if k > 0 else abs(i)
            DQ1.appendleft(nums[index])
        
        start = 0 if k > 0 else abs(k)
        end = len(nums)-k if k > 0 else len(nums)
        for i in xrange(start,end):
            DQ2.append(nums[i])
            
        for i in xrange(len(nums)):
            if k < 0:
                if DQ2: nums[i] = DQ2.popleft()
                else: nums[i] = DQ1.pop()
            else:
                if DQ1: nums[i] = DQ1.popleft()
                else: nums[i] = DQ2.popleft()
            
        
