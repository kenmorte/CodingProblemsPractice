# https://leetcode.com/problems/shortest-completing-word/description/

from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, P, W):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        if not P or not W: return ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        letters += letters.upper()
        PC = Counter(c.lower() for c in P if c in letters)
        minLength, res = float('inf'), ''
        for w in W:
            C, cancel = Counter(w), False
            for pc in PC:
                if pc not in C or PC[pc] > C[pc]:
                    cancel = True
                    break
            if cancel: continue
            if len(w) < minLength:
                minLength, res = len(w), w
        return res
