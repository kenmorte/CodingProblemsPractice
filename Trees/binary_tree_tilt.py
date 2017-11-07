# https://leetcode.com/problems/binary-tree-tilt/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.getSum(root)
        return self.result
        
    def getSum(self, root):
        if not root: return 0
        left_sum = self.getSum(root.left)
        right_sum = self.getSum(root.right)
        current_tilt = abs(left_sum - right_sum)
        self.result += current_tilt
        return left_sum + right_sum + root.val
        
        
        
        
