# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Beat 0% :P

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, P, I):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not P: return None
        Pm = {P[i]:i for i in xrange(len(P))}
        root, i = TreeNode(P[0]), I.index(P[0])
        root.left = self.build(P[0], Pm, I[:i])
        root.right = self.build(P[0], Pm, I[i+1:])
        return root
        
    def build(self, prev, P, I):
        if len(I) == 0: return None
        if len(I) == 1: return TreeNode(I[0])
        v, i = I[0], 0
        for ni, n in enumerate(I):
            if abs(P[n] - P[prev]) < abs(P[v] - P[prev]):
                v, i = n, ni
        root = TreeNode(v)
        root.left = self.build(v, P, I[:i])
        root.right = self.build(v, P, I[i+1:])
        return root
