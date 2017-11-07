# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = dict()
        for i, num in enumerate(numbers, 1):
            if num not in index_map:
                index_map[num] = []
            index_map[num].append(i)
        
        for num in index_map:
            num_to_target = target - num
            
            # Case where need two values of same value
            if num == num_to_target:
                if len(index_map[num]) > 1:
                    return index_map[num][0:2]
                continue
            
            if num_to_target in index_map:
                index_1 = index_map[num][0]
                index_2 = index_map[num_to_target][-1]
                return [min(index_1, index_2), max(index_1, index_2)]
        
        return [-1,-1]
            
