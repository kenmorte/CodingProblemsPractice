# https://leetcode.com/problems/basic-calculator-ii/description/

class Solution(object):
    def calculate(self, s):
        if not s: return
        stack = []
        sign = '+'
        digits = '0123456789'
        num = ''
        for i, c in enumerate(s):
            # print stack
            if c in digits:
                num += c
            if (c not in digits and c != ' ') or i == len(s)-1:
                if sign == '+': stack.append(int(num))
                elif sign == '-': stack.append(-int(num))
                elif sign == '/': 
                    v = stack.pop()
                    print abs(v)//int(num)
                    stack.append(v//int(num) if v >= 0 else -(abs(v)//int(num)))
                elif sign == '*': stack.append(stack.pop()*int(num))
                sign = c
                num = ''
        # print stack
        return sum(stack)
    
    def calculateFirstSolution(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return
        e = self.parse(s)
        for op in [{'*','/'},{'+','-'}]:
            e = self.eval(e,op)
        return e[0]
        
    def parse(self, e):
        res = []
        ops = {'+','-','*','/'}
        curr = ''
        for c in e:
            if c != ' ':
                if c in ops:
                    res += [int(curr), c]
                    curr = ''
                else: curr += c
        res += [int(curr)]
        return res
    
    def eval(self, e, op):
        if len(e) < 3: return e
        ops = {'+','-','*','/'}
        j, res = 1, [e[0]] if e[1] not in op else []
        lastOp = None
        while j < len(e):
            if e[j] in op:
                if lastOp in op: 
                    lastNum = res.pop()
                    res += [self.opEval(e[j], lastNum, e[j+1])]
                else:
                    if res: res.pop()
                    res += [self.opEval(e[j], e[j-1], e[j+1])]
                if e[j] in ops: lastOp = e[j]
                j += 2
            else:
                res += [e[j]]
                if e[j] in ops: lastOp = e[j]
                j += 1
        return res
    
    def opEval(self, op, L, R):
        if op == '+': return L+R
        if op == '-': return L-R
        if op == '*': return L*R
        if op == '/': return L//R
