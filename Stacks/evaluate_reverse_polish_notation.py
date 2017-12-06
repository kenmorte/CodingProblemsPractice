# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution(object):
    def evalRPN(self, T):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not T: return 0
        if len(T) == 1: return int(T[0])
        if len(T) == 2: return 0
        stack, ops = [], {'+','-','*','/'}
        for t in T:
            if t in ops:
                y,x = stack.pop(), stack.pop()
                if t == '+': stack.append(x+y)
                elif t == '-': stack.append(x-y)
                elif t == '*': stack.append(x*y)
                elif t == '/': 
                    if x*y < 0 and x % y != 0: stack.append(x/y+1)
                    else: stack.append(x/y)
            else: stack.append(int(t))
        return stack.pop()
