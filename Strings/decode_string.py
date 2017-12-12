# https://leetcode.com/problems/decode-string/description/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        stack = []
        factor, ss = '', ''
        res = ''
        for c in s:
            if c in '0123456789' and not stack: factor += c
            elif c == '[': 
                if stack: ss += c
                stack.append(0)
            elif c == ']':
                stack.pop()
                if not stack:
                    res += int(factor) * self.decodeString(ss)
                    factor, ss = '', ''
                else:
                    ss += c
            else:
                if not stack: res += c
                else: ss += c
        return res
