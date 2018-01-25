# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # O(n) time, O(n) space
        # res = []
        # count = {}
        # for n in nums:
        #     if n not in count: count[n] = 0
        #     count[n] += 1
        #     if count[n] <= 2: res.append(n)
        # nums[:len(res)] = res
        # return len(res)
        
        # O(n) time, O(1) space
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
