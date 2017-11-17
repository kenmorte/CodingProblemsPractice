# https://leetcode.com/problems/symmetric-tree/description/
# Recursive solution much more elegant, simple

from Queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        levels = []
        Q = Queue()
        Q.put((root,0))
        while not Q.empty():
            n,L = Q.get()
            if L >= len(levels): levels.append([])
            if n is None: levels[L].append(None)
            else:
                Q.put((n.left,L+1))
                Q.put((n.right,L+1))
                levels[L].append(n.val)
        for level in levels:
            if level != level[::-1]: return False
        return True
