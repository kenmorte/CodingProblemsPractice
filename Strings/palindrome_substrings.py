# https://leetcode.com/problems/palindromic-substrings/description/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindrome_count = 0
        for i in range(len(s)):
            
            # Look at all odd-length palindromes from this index
            for j in range(i+1):
                left_odd_index = i - j
                right_odd_index = i + j
                
                # Stop getting odd-length palindromes if we are out of bounds from string
                if left_odd_index < 0 or right_odd_index >= len(s):
                    break
                    
                # Stop getting odd-length palindromes if we don't see a palindrome anymore 
                # (since it's not a palindrome substring anymore, any future ones will not be palindromes as well)
                if s[left_odd_index] != s[right_odd_index]:
                    break
                
                palindrome_count += 1
            
            # Can't count even-length palindromes for first index
            if i == 0:
                continue
            
            # Get our base indices for counting even-length palindromes
            base_left_even_index = i - 1
            base_right_even_index = i
            
            # Look at all even-length palindromes form this index
            for j in range(i):
                left_even_index = i - 1 - j
                right_even_index = i + j
                
                if left_even_index < 0 or right_even_index >= len(s):
                    break
                
                if s[left_even_index] != s[right_even_index]:
                    break
                
                palindrome_count += 1
        
        return palindrome_count
