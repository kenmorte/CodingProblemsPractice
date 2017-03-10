def is_palindrome(s):
  # abba, civic, racecar
  
  for i in range(len(s)):
    left = i
    right = len(s)-1-i
    
    if s[left].lower() != s[right].lower():
      return False
  return True
  
assert is_palindrome("anna");
assert is_palindrome("AnNa");
assert is_palindrome("racecar");

assert not is_palindrome("annakendrick")
assert not is_palindrome("nsldjkfgnwelkjrlakdjfb")
