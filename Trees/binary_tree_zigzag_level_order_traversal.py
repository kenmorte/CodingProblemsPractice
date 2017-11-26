# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from Queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q, res = Queue(), []
        q.put((root,0))
        while not q.empty():
            node, L = q.get()
            if L == len(res): res.append([])
            res[L].append(node.val)
            if node.left: q.put((node.left,L+1))
            if node.right: q.put((node.right,L+1))
        for i in range(1,len(res),2):
            res[i].reverse()
        return res
