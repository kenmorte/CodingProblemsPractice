# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        occurrences = dict()
        for n in nums:
            if n not in occurrences:
                occurrences[n] = 1
            else:
                occurrences[n] += 1
        
        result = list()
        for n in occurrences:
            if occurrences[n] == 2:
                result.append(n)
        return result
        
