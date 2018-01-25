# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        if nodes[0] == '#': return len(nodes) == 1
        stack = [(0, nodes[0])]
        numChilds = {(0, nodes[0]):0}
        for index, node in enumerate(nodes[1:],1):
            if not stack: return False
            parentIndex, parentNode = stack[-1]
            numChilds[(parentIndex, parentNode)] += 1
            if numChilds[(parentIndex, parentNode)] == 2: stack.pop()
            if node != '#': 
                stack.append((index, node))
                numChilds[(index, node)] = 0
        return not stack
                
