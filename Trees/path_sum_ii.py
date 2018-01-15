# https://leetcode.com/problems/path-sum-ii/description/

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
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.dfs(root, 0, [], T, res)
        return res
    
    def dfs(self, root, sum, path, T, res):
        sum += root.val
        if not root.left and not root.right:
            if sum == T: res.append(path + [root.val])
            return
        path.append(root.val)
        if root.left: self.dfs(root.left, sum, path, T, res)
        if root.right: self.dfs(root.right, sum, path, T, res)
        path.pop()
