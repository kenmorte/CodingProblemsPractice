# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/discuss/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return 0
        self.assignParentPtrs(root, None)
        self.pathLength = float('inf')
        self.res = None
        self.dfs(self.findTarget(root, k), 0, set())
        return self.res
        
        
    def dfs(self, root, path, visited):
        if not root: return
        if root in visited: return
        visited.add(root)
        if not root.left and not root.right:
            if path < self.pathLength:
                self.pathLength = path
                self.res = root.val
            visited.remove(root)
            return
        self.dfs(root.left, path+1, visited)
        self.dfs(root.right, path+1, visited)
        self.dfs(root.parent, path+1, visited)
        visited.remove(root)
                
        
    def findTarget(self, root, k):
        if not root: return None
        if root.val == k: return root
        left, right = self.findTarget(root.left, k), self.findTarget(root.right, k)
        return left if left else right
        
    def assignParentPtrs(self, root, parent):
        if not root: return
        root.parent = parent
        self.assignParentPtrs(root.left, root)
        self.assignParentPtrs(root.right, root)
