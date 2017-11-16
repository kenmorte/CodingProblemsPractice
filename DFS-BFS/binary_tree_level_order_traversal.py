# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from Queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        Q = Queue()
        Q.put((root,0))
        res = []
        while not Q.empty():
            n, L = Q.get()
            if n.left: Q.put((n.left,L+1))
            if n.right: Q.put((n.right,L+1))
            if L < len(res): res[L].append(n.val)
            else: res.append([n.val])
        return res
