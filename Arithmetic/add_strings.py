# https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, a, b):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not a or a == '0': return b
        if not b or b == '0': return a
        a = ('0'*max(0,len(b)-len(a))) + a
        b = ('0'*max(0,len(a)-len(b))) + b
        c = [0 for _ in xrange(len(a))]
        res = [0 for _ in xrange(len(a))]
        for i in xrange(len(a)-1, -1, -1):
            res[i], c[i-1] = self.addDigits(a[i], b[i], c[i])
        return (str(c[-1]) if c[-1] != '0' else '') + ''.join(res)
    
    def addDigits(self, a, b, c):
        s = int(a) + int(b) + int(c)
        return (str(s%10),str(s//10))
