# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.resultRow = 0
        self.resultVal = root.val
        self.dfs(root.left, 1)
        self.dfs(root.right, 1)
        return self.resultVal
        
    def dfs(self, root, row):
        if not root:
            return
        if row > self.resultRow:
            self.resultRow = row
            self.resultVal = root.val
        self.dfs(root.left, row + 1)
        self.dfs(root.right, row + 1)
        
