# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = (max(len(b)-len(a), 0) * '0') + a
        b = (max(len(a)-len(b), 0) * '0') + b
        c = '0'
        res = ''
        for i in xrange(len(a)-1,-1,-1):
            sum, carry = self.add(a[i],b[i],c)
            res, c = res + sum, carry
        res += c if c == '1' else ''
        return res[::-1]
            
    def add(self, a, b, c):
        binary = a+b+c
        if binary == '000': return ('0','0')
        if binary in {'001', '010', '100'}: return ('1','0')
        if binary in {'011', '101', '110', }: return ('0','1')
        return ('1','1')
