# https://leetcode.com/problems/minimum-window-substring/description/

class Solution(object):
    def minWindow(self, S, T):
        if not S or not T: return ''
        if len(T) > len(S): return ''
        V, C = {}, {c:0 for c in S}
        for c in T:
            if c not in V: V[c] = 0
            V[c] += 1
        i,j = 0,0
        counter, res = 0, None
        while j < len(S):
            if S[j] in V:
                C[S[j]] += 1
                counter += 1 if C[S[j]] <= V[S[j]] else 0
            if counter == len(T):
                while counter == len(T):
                    if S[i] in V:
                        C[S[i]] -= 1
                        counter -= 1 if C[S[i]] < V[S[i]] else 0
                    i += 1
                if not res: res = S[i-1:j+1]
                else: res = min(res, S[i-1:j+1], key=len)
            j += 1
        return res if res else ''
