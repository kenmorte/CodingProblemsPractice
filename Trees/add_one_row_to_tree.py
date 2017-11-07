# https://leetcode.com/problems/add-one-row-to-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(v)
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        self.dfs(root, v, d, 1)
        return root
        
    def dfs(self, root, v, d, current_level):
        if not root: return
        if current_level == d-1:
            orig_left_subtree = root.left
            orig_right_subtree = root.right
            
            new_left_subtree = TreeNode(v)
            new_right_subtree = TreeNode(v)
            
            new_left_subtree.left = orig_left_subtree
            new_right_subtree.right = orig_right_subtree
            
            root.left = new_left_subtree
            root.right = new_right_subtree
        else:
            self.dfs(root.left, v, d, current_level + 1)
            self.dfs(root.right, v, d, current_level + 1)
        
