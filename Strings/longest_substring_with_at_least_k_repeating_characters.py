# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k: return 0
        m = ('',float('inf'))
        d = dict()
        for c in s:
            if c not in d: d[c] = 0
            d[c] += 1
        for c in d:
            if d[c] < m[1]: m = (c,d[c])
        if m[1] >= k: return len(s)
        return max(self.longestSubstring(t,k) for t in s.split(m[0]))
    
    def FirstSolutionlongestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k <= 0: return 0
        
        n = len(s)
        if k == 1: return n
        if n < k: return 0
        res = 0
        
        def isValid(d,k):
            for n in d.values():
                if n < k: return False
            return True
        
        d = dict()
        prev = None
        for i,c in enumerate(s):
            if c not in d: d[c] = []
            if prev != c: d[c].append(i)
            prev = c
        
        for c in d:
            for i in d[c]:
                # i = s.index(c)
            
                # Occurrences of each character
                L, R, B = {c:1}, {c:1}, {c:1}

                # Traverse left
                j = i-1
                while j >= 0:
                    if s[j] not in L: L[s[j]] = 0
                    L[s[j]] += 1
                    if isValid(L,k): 
                        # print 'left', s[j:i+1], L
                        res = max(res, i-j+1)
                    j -= 1

                # Traverse right
                j = i+1
                while j < n:
                    if s[j] not in R: R[s[j]] = 0
                    R[s[j]] += 1
                    if isValid(R,k): 
                        # print 'right', s[i:j+1], R
                        res = max(res, j-i+1)
                    j += 1

                # Traverse left + right
                jL, jR = i-1, i+1
                while True:
                    # Check if current occurrences are valid
                    valid_jL, valid_jR = max(0, jL), min(jR, n-1)

                    if s[valid_jL] not in B: B[s[valid_jL]] = 0
                    if s[valid_jR] not in B: B[s[valid_jR]] = 0
                    if jL >= 0: B[s[valid_jL]] += 1
                    if jR < n: B[s[valid_jR]] += 1
                    if isValid(B,k): 
                        # print 'both', s[valid_jL:valid_jR+1], B
                        res = max(res, valid_jR-valid_jL+1)

                    # Advance/break checking left and right
                    if jL <= 0 and jR >= n-1: break
                    jL -= 1
                    jR += 1
                
        return res
                
        
