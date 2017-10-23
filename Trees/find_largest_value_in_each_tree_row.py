# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.max_map = dict()
        self.dfs(root, 0)
        result = [0 for k in range(max(self.max_map.keys()) + 1)]
        for level in self.max_map:
            result[level] = self.max_map[level]
        return result
        
        
    def dfs(self, root, level):
        if not root:
            return
        if level not in self.max_map:
            self.max_map[level] = root.val
        else:
            self.max_map[level] = max(self.max_map[level], root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
