# https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs: return []
        d = dict()
        for s in strs:
            g = dict()
            for c in s:
                if c not in g: g[c] = 0
                g[c] += 1
            g = frozenset((c,g[c]) for c in g)
            if g not in d: d[g] = [s]
            else: d[g].append(s)
        return d.values()
