# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        nums = [i for i in xrange(1,n+1)]
        return self.sortedArrayToBSTList(nums)
        
    def sortedArrayToBSTList(self, arr):
        if not arr: return [None]
        if len(arr) == 1: return [TreeNode(arr[0])]
        res = []
        for i in xrange(len(arr)):
            for leftSubtree in self.sortedArrayToBSTList(arr[:i]):
                for rightSubtree in self.sortedArrayToBSTList(arr[i+1:]):
                    root = TreeNode(arr[i])
                    root.left = leftSubtree
                    root.right = rightSubtree
                    res.append(root)
        return res
