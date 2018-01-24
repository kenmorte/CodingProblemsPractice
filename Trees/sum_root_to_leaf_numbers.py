# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        self.dfs(root, nums, '')
        return sum([int(s) for s in nums]) if nums else 0
    
    def dfs(self, root, nums, s):
        if not root: return
        s += str(root.val)
        if not root.left and not root.right:
            nums.append(s)
            return
        if root.left: self.dfs(root.left, nums, s)
        if root.right: self.dfs(root.right, nums, s)
        
