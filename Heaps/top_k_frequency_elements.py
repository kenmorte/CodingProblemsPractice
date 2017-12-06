# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_map = dict()
        max_frequency = 0
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1
            max_frequency = max(max_frequency, frequency_map[num])
        
        top_frequency_list = [[] for i in range(max_frequency + 1)]
        for frequency in frequency_map:
            top_frequency_list[frequency_map[frequency]].append(frequency)
        
        result = []
        i = len(top_frequency_list) - 1
        while i >= 0:
            if not top_frequency_list[i]:
                i -= 1
                continue
            if len(result) == k:
                return result
            for num in top_frequency_list[i]:
                if len(result) < k: result.append(num)
                else: return result
            i -= 1
        return result
