# https://leetcode.com/problems/longest-univalue-path/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.longestPath(root)
    
    def longestPath(self, root):
        if not root: return 0
        usingRoot = self.calculateLongestPath(root.left, root.val) + self.calculateLongestPath(root.right, root.val)
        usingRootLeft = self.longestPath(root.left)
        usingRootRight = self.longestPath(root.right)
        return max(usingRoot, usingRootLeft, usingRootRight)
    
    def calculateLongestPath(self, root, val):
        if not root: return 0
        if root.val != val: return 0
        return 1 + max(self.calculateLongestPath(root.left, val), self.calculateLongestPath(root.right, val))
    
    
