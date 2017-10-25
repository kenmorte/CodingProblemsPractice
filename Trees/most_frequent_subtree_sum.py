# https://leetcode.com/problems/most-frequent-subtree-sum/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.sum_map = dict()
        self.dfs(root)
        
        max_occurrence_sum = float('-inf')
        for sum in self.sum_map:
            if self.sum_map[sum] > max_occurrence_sum:
                max_occurrence_sum = self.sum_map[sum]
        
        result = []
        for sum in self.sum_map:
            if self.sum_map[sum] == max_occurrence_sum:
                result.append(sum)
        return result
        
        
    def dfs(self, root):
        if not root:
            return 0
        sum_at_this_node = root.val + self.dfs(root.left) + self.dfs(root.right)
        if sum_at_this_node not in self.sum_map:
            self.sum_map[sum_at_this_node] = 0
        self.sum_map[sum_at_this_node] += 1
        return sum_at_this_node
