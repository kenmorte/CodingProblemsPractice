# https://leetcode.com/problems/serialize-and-deserialize-bst/description/

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
        res = str(root.val)
        if root.left: res += ',(' + self.serialize(root.left) + ')'
        if root.right:
            if not root.left: res += ',()'
            res += ',(' + self.serialize(root.right) + ')'
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        if ',' not in data: return TreeNode(int(data))
        index = data.index(',')
        root = TreeNode(int(data[:index]))
        index, stack = index+1, 0
        left, right = [index+1,None], [None,None]
        while index < len(data):
            if data[index] == '(': stack += 1
            elif data[index] == ')':
                stack -= 1
                if not stack:
                    if not left[1]:
                        left[1] = index
                        right[0] = index+3
                    elif not right[1]: right[1] = index
            index += 1
        if left[0] and left[1] and left[0] < len(data) and left[1] < len(data) and left[1] > left[0]:
            root.left = self.deserialize(data[left[0]:left[1]])
        if right[0] and right[1] and right[0] < len(data) and right[1] < len(data) and right[1] > right[0]:
            root.right = self.deserialize(data[right[0]:right[1]])
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
