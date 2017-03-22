# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return (p and q and p.val == q.val and \
                    self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)) or \
                (not p and not q)
