# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

class TreeNode:
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        root = TreeNode(nums[-1],0)
        counts = [0 for _ in nums]
        for i in xrange(len(nums)-2, -1, -1):
            counts[i] = self.insert(root, nums[i], 0)
        return counts
    
    def insert(self, root, n, countLess):
        if n <= root.val:
            root.count += 1
            if root.left: return self.insert(root.left, n, countLess)
            root.left = TreeNode(n,0)
        else:
            countLess += 1 + root.count
            if root.right: return self.insert(root.right, n, countLess)
            root.right = TreeNode(n,0)
        return countLess
