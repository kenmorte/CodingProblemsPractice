# https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, S):
        """
        :type s: str
        :rtype: bool
        """
        if not S: return True
        validChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        i, j = 0, len(S)-1
        while i < j:
            L, R = S[i].upper(), S[j].upper()
            while L not in validChars:
                i += 1
                if i == len(S): break
                L = S[i].upper()
            while R not in validChars:
                j -= 1
                if j == -1: break
                R = S[j].upper()
            if i < j and L != R: return False
            i += 1
            j -= 1
        return True
