# https://leetcode.com/problems/license-key-formatting/description/

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Runs faster
        curr = ''
        res = []
        for c in reversed(S):
            if c == '-': continue
            curr = c.upper() + curr
            if len(curr) == K:
                res += [curr]
                curr = ''
        if curr: res += [curr]
        return '-'.join(reversed(res))
        
        # Runs really slow
        # curr = ''
        # res = ''
        # for c in reversed(S):
        #     if c == '-': continue
        #     curr = c.upper() + curr
        #     if len(curr) == K:
        #         res = '-' + curr + res
        #         curr = ''
        # res = curr + res
        # return res if not res or res[0] != '-' else res[1:]
