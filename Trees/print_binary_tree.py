# https://leetcode.com/problems/print-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return []
        m = self.getHeight(root)
        n = (2**m) - 1
        result = [['' for col in range(n)] for row in range(m)]
        self.fillResultTree(result, root, 0, 0, n)
        return result
        
    def fillResultTree(self, result, root, level, leftBound, rightBound):
        if not root: return
        if leftBound == rightBound: return
        rootIndex = (leftBound + rightBound) // 2
        result[level][rootIndex] = str(root.val)
        self.fillResultTree(result, root.left, level+1, leftBound, rootIndex)
        self.fillResultTree(result, root.right, level+1, rootIndex+1, rightBound)
        
        
    def getHeight(self, root):
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
