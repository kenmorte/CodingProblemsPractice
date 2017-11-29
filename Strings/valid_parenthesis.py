# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        stack = []
        for c in s:
            if c in {'(', '{', '['}: stack.append(c)
            else:
                if len(stack) == 0: return False
                if (stack[-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}') or (stack[-1] == '[' and c == ']'):
                    stack.pop()
                else: return False
        return len(stack) == 0
