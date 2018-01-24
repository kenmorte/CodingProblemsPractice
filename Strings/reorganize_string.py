# https://leetcode.com/problems/reorganize-string/description/

from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = Counter(S)
        res = ''
        while count:
            a = max(count, key=lambda c: count[c])
            n = count[a]
            del count[a]
            if not count: 
                if n > 1: return ''
                b = ''
            else: b = max(count, key=lambda c: count[c])
            addA = True
            while n:
                if addA:
                    res += a
                    n -= 1
                else:
                    res += b
                    count[b] -= 1
                    if not count[b]:
                        del count[b]
                        if not count: 
                            if n > 1: return ''
                            b = ''
                        else: b = max(count, key=lambda c: count[c])
                addA = not addA
        return res
                
                
            
