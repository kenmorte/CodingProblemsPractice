# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# NOTE: Could've used in-order traversal on this one :P

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('inf')
        self.dfs(root)
        return self.result
        
    def dfs(self, root):
        if not root: return
        val_to_compare = root.val
        self.compareLeft(root.left, val_to_compare) # Keep traversing right from the left subtree
        self.compareRight(root.right, val_to_compare) # Keep traversing left from the right subtree
        self.dfs(root.left)
        self.dfs(root.right)
        
    def compareLeft(self, root, val_to_compare):
        if not root: return
        if not root.right: self.result = min(self.result, abs(val_to_compare - root.val))
        self.compareLeft(root.right, val_to_compare)
        
    def compareRight(self, root, val_to_compare):
        if not root: return
        if not root.left: self.result = min(self.result, abs(val_to_compare - root.val))
        self.compareRight(root.left, val_to_compare)

    
