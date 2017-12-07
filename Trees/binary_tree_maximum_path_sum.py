# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = float('-inf')
        
    def maxPathSum(self, root):
        self.maxPathSumHelper(root)
        return self.res
    
    def maxPathSumHelper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return float('-inf')
        max_at_left = self.maxPathSumHelper(root.left)
        max_at_right = self.maxPathSumHelper(root.right)
        max_here = max(root.val, root.val+max_at_left, root.val+max_at_right)
        self.res = max(self.res, max_here, root.val+max_at_left+max_at_right)
        return max_here
