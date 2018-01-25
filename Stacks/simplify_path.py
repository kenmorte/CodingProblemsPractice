# https://leetcode.com/problems/simplify-path/description/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = ['']
        for directory in path.split('/'):
            if directory == '.' or not directory: continue
            elif directory == '..':
                if len(stack) > 1: stack.pop()
            else: stack.append(directory)
        return '/' if not stack or (len(stack) == 1 and not stack[0]) else '/'.join(stack)
