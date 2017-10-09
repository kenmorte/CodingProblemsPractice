# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        if not root:
            return []
        
        result = []
        self.map = dict()
        self.dfs(root, 0)
        
        for index in sorted(self.map.keys()):
            result.append(sum(self.map[index]) * 1.0 / len(self.map[index]))
        return result
        
    def dfs(self, root, level):
        if not root:
            return
        if level not in self.map:
            self.map[level] = []
        self.map[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
