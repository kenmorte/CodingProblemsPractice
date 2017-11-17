# https://leetcode.com/problems/ransom-note/description/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_map = dict()
        ransom_map = dict()
        
        for c in ransomNote:
            if c in ransom_map:
                ransom_map[c] += 1
            else:
                ransom_map[c] = 1
        
        for c in magazine:
            if c in mag_map:
                mag_map[c] += 1
            else:
                mag_map[c] = 1
                
        for ransom_char in ransom_map:
            if ransom_char not in mag_map or ransom_map[ransom_char] > mag_map[ransom_char]:
                return False
        return True
        
