# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

from Queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res, Q, i = '', Queue(), 0
        Q.put((root, 'null', -1, 0))
        while not Q.empty():
            node, parent, parentIndex, isLeft = Q.get()
            res += str(node.val) + '|' + str(i) + '|' + parent + '|' + str(parentIndex) + '|' + str(isLeft) + '_'
            if node.left: Q.put((node.left, str(node.val), i, 1))
            if node.right: Q.put((node.right, str(node.val), i, 0))
            i += 1
        return res[:len(res)-1]
                    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nodes, data, root = {}, data.split('_'), None
        for s in data:
            val, i, p, pi, isLeft = tuple(s.split('|'))
            curr = TreeNode(int(val))
            nodes[val+'|'+i] = curr
            if p != 'null':
                parent = nodes[p+'|'+pi]
                if int(isLeft): parent.left = curr
                else: parent.right = curr
            else: root = curr
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
