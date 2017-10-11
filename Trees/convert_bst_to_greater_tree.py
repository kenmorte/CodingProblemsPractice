# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.reverseInorderTrasversal(root)
        return root
        
    def reverseInorderTrasversal(self, root):
        if not root:
            return  
        self.reverseInorderTrasversal(root.right)
        self.sum += root.val
        root.val = self.sum
        self.reverseInorderTrasversal(root.left)
        
