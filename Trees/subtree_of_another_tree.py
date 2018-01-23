# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return all([self.inorder(t) in self.inorder(s), 
                   self.preorder(t) in self.preorder(s), 
                   self.postorder(t) in self.postorder(s)])
        
    def inorder(self, root):
        if not root: return '_'
        return self.inorder(root.left) + str(root.val) + self.inorder(root.right)
    
    def postorder(self, root):
        if not root: return '_'
        return self.postorder(root.left) + self.postorder(root.right) + str(root.val)
    
    def preorder(self, root):
        if not root: return '_'
        return str(root.val) + self.preorder(root.left) + self.preorder(root.right)
