# https://leetcode.com/problems/number-of-atoms/description/

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        count = self.parse(formula, 1)
        res = ''
        for el in sorted(count):
            res += el + (str(count[el]) if count[el] > 1 else '')
        return res
        
    
    def parse(self, formula, globalFactor):
        if not formula: return {}
        
        stack = []
        num = ''
        res = {}
        
        for c in formula:
            if not stack: stack.append([c if c != '(' else '',1,[] if c != '(' else [0],c=='('])
            else:
                if c == ')':
                    stack[-1][2].pop()
                    if stack[-1][2]: stack[-1][0] += c
                    num = ''
                elif stack[-1][2]:
                    stack[-1][0] += c
                    if c == '(': stack[-1][2].append(0)
                elif c in '0123456789':
                    num += c
                elif c == '(':
                    stack[-1][1] = int(num) if num else 1
                    stack.append(['',1,[0],True])
                    num = ''
                elif c.upper() == c:
                    stack[-1][1] = int(num) if num else 1
                    stack.append([c,1,[],False])
                    num = ''
                else: stack[-1][0] += c
        stack[-1][1] = int(num) if num else 1
        
        while stack:
            element, factor, _, needsToBeParsed = stack.pop()
            if needsToBeParsed: 
                parsedFormula = self.parse(element,factor)
                for el in parsedFormula:
                    if el in res: res[el] += parsedFormula[el]
                    else: res[el] = parsedFormula[el]
            elif element in res: res[element] += factor
            else: res[element] = factor
                
        for element in res: res[element] *= globalFactor
        return res
    
