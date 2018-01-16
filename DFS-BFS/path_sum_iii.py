# https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, T):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root, 0, T, set())
        return self.res
    
    def dfs(self, root, sum, T, resetted):
        sum += root.val
        if sum == T: self.res += 1
        if root.left:
            self.dfs(root.left, sum, T, resetted)
            if root not in resetted: self.dfs(root.left, 0, T, resetted)
        if root.right:
            self.dfs(root.right, sum, T, resetted)
            if root not in resetted: self.dfs(root.right, 0, T, resetted)
        resetted.add(root)
