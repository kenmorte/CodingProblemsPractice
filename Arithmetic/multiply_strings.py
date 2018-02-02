# https://leetcode.com/problems/multiply-strings/description/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = '0'
        for factor, digit in enumerate(num2[::-1]):
            product = self.multiplyWithDigit(num1, int(digit)) + ('0'*factor)
            sum = self.add(sum, product)
            sum = '0' if not sum else sum
        return sum
    
    def add(self, num1, num2):
        if num1 == '0': return num2.lstrip('0')
        if num2 == '0': return num1.lstrip('0')
        carry = 0
        res = ''
        num1 = ('0'*max(0, len(num2)-len(num1))) + num1
        num2 = ('0'*max(0, len(num1)-len(num2))) + num2
        for i in xrange(len(num1)-1,-1,-1):
            sum = str(int(num1[i]) + int(num2[i]) + carry)
            sum = '0' + sum if len(sum) == 1 else sum
            carry = int(sum[0])
            res += sum[1]
        res += str(carry) if carry else ''
        return res[::-1].lstrip('0')
        
    def multiplyWithDigit(self, num, digit):
        if digit == '0': return '0'
        res = ''
        carry = 0
        for n in num[::-1]:
            product = str((int(n) * digit) + carry)
            if len(product) == 1: product = '0' + product
            res += product[1]
            carry = int(product[0])
        res += str(carry) if carry else ''
        return res[::-1]
            
