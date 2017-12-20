# https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        nums = []
        dp1, dp2 = {None:0}, {None:0}
        self.dfs(root, dp1, dp2)
        return max(dp1[root], dp2[root])
    
    def dfs(self, root, dp1, dp2):
        if not root: return 0
        if not root.left and not root.right:
            dp1[root] = root.val
            dp2[root] = 0
            return
        self.dfs(root.left, dp1, dp2)
        self.dfs(root.right, dp1, dp2)
        dp1[root] = max(root.val + dp2[root.left] + dp2[root.right], dp1[root.left] + dp1[root.right])
        dp2[root] = max(dp1[root.left] + dp1[root.right], dp2[root.left] + dp2[root.right])
