# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        occurrence_map = dict()
        max_occurrence = 0
        for c in s:
            if c not in occurrence_map:
                occurrence_map[c] = 1
            else:
                occurrence_map[c] += 1
            max_occurrence = max(max_occurrence, occurrence_map[c])
        
        occurrence_list = [[] for n in range(max_occurrence)]
        for c in occurrence_map:
            occurrence_list[occurrence_map[c]-1].append(c)
        
        result = ''
        for i in range(len(occurrence_list)-1, -1, -1):
            L = occurrence_list[i]
            for c in L:
                result += c * (i+1)
        return result
        
        
