# https://leetcode.com/problems/word-pattern/description/

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split = str.split()
        if len(pattern) != len(split): return False
        map = {}
        for i, c in enumerate(pattern):
            if c not in map: 
                if split[i] in map.values(): return False
                map[c] = split[i]
            elif map[c] != split[i]: return False
        return True
