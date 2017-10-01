# https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val >= L and root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else: # root.val < L:
            return self.trimBST(root.right, L, R)
        
        
        # Look at the root node first
        #   If it within the bounds => 
        #       keep that node
        #       recursively go through the left and right nodes
        #   If it's greater than the top bound => we get rid of that root node + all the other nodes on the right
        #   If it's less than the bottom bound => we get rid of that root node + all the other nodes on the left
