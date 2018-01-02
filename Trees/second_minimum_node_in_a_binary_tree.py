# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        return self.dfs(root, root.val)
    
    def dfs(self, root, val):
        if not root: return -1
        if root.val != val: return root.val
        if not root.left and not root.right: return -1
        res = left = self.dfs(root.left, val)
        if left == -1: res = self.dfs(root.right, val)
        else: 
            right = self.dfs(root.right, val)
            if right == -1: return res
            else: return min(res, right)
        return res
