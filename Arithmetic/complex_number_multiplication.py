# https://leetcode.com/problems/complex-number-multiplication/description/

class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1.split('+') # [ a, bi ]
        num2 = num2.split('+') # [c , di ]
        a = int(num1[0])
        b = int(num1[1][:len(num1[1])-1])
        c = int(num2[0])
        d = int(num2[1][:len(num2[1])-1])
        
        result_a = (a*c) - (b*d)
        result_b = (a*d) + (b*c)
        return str(result_a) + '+' + str(result_b) + 'i'
