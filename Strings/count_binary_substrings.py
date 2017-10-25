# https://leetcode.com/problems/count-binary-substrings/description/

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 0
        
        changed_indices = []
        current_val = s[0]
        count_so_far = 0
        for c in s:
            if c == current_val:
                count_so_far += 1
            else:
                changed_indices.append(count_so_far)
                count_so_far = 1
                current_val = c
        changed_indices.append(count_so_far)
        
        result = 0
        for i in range(len(changed_indices)-1):
            result += min(changed_indices[i], changed_indices[i+1])
        return result
        
