# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        max_left, max_right, res = {0:0}, {0:0}, 0
        self.dfs(root, max_left, max_right, 1, 0)
        for level in max_left: res = max(res, abs(max_right[level] - max_left[level]))
        return res+1
        
    
    def dfs(self, root, max_left, max_right, level, pos):
        if not root: return
        
        left = 2*pos
        right = 2*pos+1
        
        if root.left: 
            max_left[level] = min(max_left.get(level, float('inf')), left)
            max_right[level] = max(max_right.get(level, float('-inf')), left)
        if root.right:
            max_left[level] = min(max_left.get(level, float('inf')), right)
            max_right[level] = max(max_right.get(level, float('-inf')), right)
        
        self.dfs(root.left, max_left, max_right, level+1, left)
        self.dfs(root.right, max_left, max_right, level+1, right)
        
        
