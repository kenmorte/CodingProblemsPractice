# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.nodes = dict()
        self.dfs(root)
        for node in self.nodes:
            if k - node == node:
                if self.nodes[node] > 2:
                    return True
                continue
            if k - node in self.nodes:
                return True
        return False
        
    def dfs(self, root):
        if not root:
            return
        if root.val not in self.nodes:
            self.nodes[root.val] = 1
        else:
            self.nodes[root.val] += 1
        self.dfs(root.left)
        self.dfs(root.right)
