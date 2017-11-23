# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left: return
        L, R = root.left, root.right
        while L and R:
            L.next = R
            L, R = L.right, R.left
        self.connect(root.left)
        self.connect(root.right)
        
