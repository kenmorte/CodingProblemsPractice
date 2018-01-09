# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderDFS(root, res)
        return res
    
    def inorderDFS(self, root, res):
        if not root: return
        DQ = deque([[root, 0]])
        while DQ:
            node, F = tuple(DQ[0])
            if not F:
                DQ[0][1] = 1
                if node.left: DQ.appendleft([node.left, 0])
            else:
                res += [node.val]
                right = node.right
                DQ.popleft()
                if right: DQ.appendleft([right, 0])
                
        
