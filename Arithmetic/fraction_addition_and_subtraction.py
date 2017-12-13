# https://leetcode.com/problems/fraction-addition-and-subtraction/description/

from math import sqrt

class Solution(object):
    def fractionAddition(self, E):
        """
        :type expression: str
        :rtype: str
        """
        if not E: return ''
        isPos, isNumerator, num = True, E[0] in '0123456789', ''
        N, D = [], []
        for c in E:
            if c in '+-/':
                if num:
                    if isNumerator: N.append(int(num) * (1 if isPos else -1))
                    else: D.append(int(num) * (1 if isPos else -1))
                    isPos = True
                num = ''
                isNumerator = not isNumerator
                if c == '+': isPos = True
                elif c == '-': isPos = False
            else: num += c
                
        if isNumerator: N.append(int(num) * (1 if isPos else -1))
        else: D.append(int(num) * (1 if isPos else -1))
            
        denominator = self.product(D)
        for i in xrange(len(N)): N[i] *= denominator // D[i]
        numerator = sum(N)
        if not numerator: return '0/1'
        isPos = numerator > 0
        numerator = abs(numerator)
        GCD = self.maxGCD(numerator, denominator)
        sign = '' if isPos else '-'
        return sign + str(numerator // GCD) + '/' + str(denominator // GCD)
        
    def maxGCD(self, n1, n2):
        res = 1
        f1, f2 = self.factors(n1), self.factors(n2)
        for f in f1:
            if f in f2: res = max(res, f)
        return res
    
    def product(self, nums):
        res = 1
        for n in nums: res *= n
        return res
    
    def factors(self, n):
        res = set()
        for i in xrange(1, int(sqrt(n)+1)):
            if n%i == 0:
                res.add(i)
                res.add(n//i)
        print res
        return res
    
