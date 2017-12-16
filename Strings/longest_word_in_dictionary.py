# https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words: return ''
        trie = {'isWord': False, 'children': {}}
        
        for word in words:
            curr = trie
            for c in word:
                if c not in curr['children']: curr['children'][c] = {'isWord': False, 'children': {}}
                curr = curr['children'][c]
            curr['isWord'] = True
        
        self.res = ''
        self.dfs(trie, '')
        return self.res
        
    def dfs(self, root, curr):
        if not root: return
        for c in root['children']:
            if root['children'][c]['isWord']:
                self.dfs(root['children'][c], curr+c)
        if root['isWord']:
            if len(curr) > len(self.res): self.res = curr
            elif len(curr) == len(self.res): self.res = min(self.res, curr)
