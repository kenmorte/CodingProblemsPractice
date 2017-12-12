# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p: return []
        if len(p) > len(s): return []
        
        A, curr, res = {}, {}, []
        i = j = 0
        
        for c in p:
            if c not in A: A[c] = 0
            A[c] += 1
        
        while j < len(s):
            c = s[j]
            if c not in A: 
                curr = {}
                i = j+1
            else:
                if c not in curr:
                    curr[c] = 1
                    if curr == A:
                        res.append(i)
                        # print curr, A, res
                else:
                    if curr[c] == A[c]:
                        while c in curr and curr[c] == A[c]:
                            curr[s[i]] -= 1
                            if curr[s[i]] <= 0: 
                                # print 'before', curr
                                del curr[s[i]]
                                # print 'after', curr
                            i += 1
                            if curr == A: 
                                res.append(i)
                                # print curr, A, res
                        if c not in curr: curr[c] = 0
                            
                    curr[c] += 1
                    if curr == A:
                        res.append(i)
                        # print curr, A, res
            j += 1
        return res
                        
