# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        t = {'1':'*', '2':'abc', '3':'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.dfs(digits, t, '', res)
        return res
        
    def dfs(self, s, t, curr, res):
        if not s:
            if curr: res.append(curr)
            return
        for c in t[s[0]]:
            self.dfs(s[1:], t, curr+c, res)
