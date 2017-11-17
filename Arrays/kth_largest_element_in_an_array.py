# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return None
        if k <= 0: return None
            
        nums.sort()
        return nums[len(nums)-k]
    
    def swap(self, a, i, j):
        if not a: return
        if i is None or j is None: return
        if i < 0 or i >= len(a) or j < 0 or j >= len(a): return
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        
    def partition(self, a):
        if len(a) <= 1: return a
        left, right = 1, len(a)-1
        pivot = a[0]
        while left < right:
            while a[left] < pivot: left += 1
            while a[right] > pivot: right -= 1
            if left < right: self.swap(a, left, right)
        
        self.swap(a, 0, right)
        
        # return the index of the pivot
        return right
    
    def quicksort(self, a):
        if len(a) <= 1: return
        print a
        pivot_index = self.partition(a)
        self.quicksort(a[:pivot_index])
        self.quicksort(a[pivot_index+1:])
