# https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        places = []
        factor = 1
        for c in str(num)[::-1]:
            places = [int(c)*factor] + places
            factor *= 10
        return ''.join(self.convert(n) for n in places)
    
    def convert(self, n):
        if n <= 0: return ''
        special = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        if n in special: return special[n]
        t = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        for comp,s in t: 
            if n >= comp: return s*(n//comp) + self.convert(n%comp)
        return ''
            
