# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        self.result = None
        self.isInTree(root, p, q)
        return self.result
        
    def isInTree(self, root, p, q):
        if not root:
            return False
        
        isInRoot = root == p or root == q
        isInLeftSubtree = self.isInTree(root.left, p, q)
        isInRightSubtree = self.isInTree(root.right, p, q)
        isLCA = (isInRoot and (isInLeftSubtree or isInRightSubtree)) or (isInLeftSubtree and isInRightSubtree)
        
        if isLCA and self.result is None:
            self.result = root
        
        return isInRoot or isInLeftSubtree or isInRightSubtree
        
        
        
