# https://leetcode.com/problems/find-duplicate-subtrees/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        d = {}
        res = set()
        added = set()
        self.inorder(root, d, res, added, False)
        return list(res)
        
    def inorder(self, root, d, res, added, fromLeft):
        if not root: return 'L' if fromLeft else 'R'
        inorder = self.inorder(root.left, d, res, added, True) + str(root.val) + self.inorder(root.right, d, res, added, False)
        if root.val not in d: d[root.val] = set()
        if inorder in d[root.val] and inorder not in added:
            added.add(inorder)
            res.add(root)
        else: d[root.val].add(inorder)
        return inorder
        
