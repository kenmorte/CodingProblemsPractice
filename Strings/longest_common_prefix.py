# https://leetcode.com/problems/longest-common-prefix/description/

class Node:
    def __init__(self, pre, count):
        self.pre = pre
        self.count = count
        self.children = dict()
            

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        minStr = min(strs, key=len)
        for i in range(len(minStr)):
            for s in strs:
                if s[i] != minStr[i]: return minStr[:i]
        return minStr
    
    def longestCommonPrefixFirstSolution(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        return self.getLongestPrefix(self.buildPrefixTree(strs), len(strs))
        
    def buildPrefixTree(self, strs):
        res = Node('', 0)
        for s in strs:
            curr = res
            curr.count += 1

            for c in s:
                if c not in curr.children:
                    curr.children[c] = Node(c, 0)
                curr.children[c].count += 1
                curr = curr.children[c]
        return res
        
    def getLongestPrefix(self, root, n):
        for child in root.children:
            if root.children[child].count == n:
                return root.pre + self.getLongestPrefix(root.children[child], n)
        return root.pre
