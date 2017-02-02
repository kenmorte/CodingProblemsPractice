# Take in an Int array and move all the zeroes to the end in place. It doesn’t 
#   matter how the non-zero numbers are ordered. Preferably as efficient and as 
#   space efficient as possible.
#   Example: Input : [ 3, 0, 2, 0, 0, 4, 1, 0 ], 
#            Accepted Output: [ 4, 2, 3, 1, 0, 0, 0, 0 ] 



# Sorting + Reversing --> O(nlogn) time, O(1) space for in-place sort + reverse? 
#   Reversing could possibly take O(n) space...

# Count # of zeros, all nonzeros go to a new list, add rest of zeros
#   to the end --> O(n) time, O(n) space

# Preferably, we would want have an in-place mechanism to move numbers around
#   Keep two pointers, left and right!
#   [ 1, 0, 2, 0, 0, 4, 1, 1 ] --> left @ 0, right @ 7
#   [ 3, 1, 2, 0, 0, 4, 0, 0 ] --> left @ 1, right @ 6 ---> SWAP! 
#   [ 3, 1, 2, 0, 0, 4, 0, 0 ] --> left @ 2, right @ 5 ---> both nonzeros --> advance right pointer
#   [ 3, 1, 2, 0, 0, 4, 0, 0 ] --> left @ 2, right @ 4 ---> SWAP! .... continue on

#   leftv = 0, rightv = 0 --> advance right pointer
#   leftv = nonzero, rightv = 0 --> advance both pointers
#   leftv = 0, rightv = nonzero --> SWAP!, advance both pointers
#   leftv = nonezero, rightv = nonzero --> advance left pointer
#   
#   Time complexity = O(n), Space complexity = O(1)


def zero_end(l: [int]) -> [int]:
  if len(l) == 0 or len(l) == 1:
    return l
  
  left = 0
  right = len(l)-1
  
  while (left < right):
    if l[left] == 0 and l[right] == 0:
      right -= 1
    elif l[left] != 0 and l[right] == 0:
      left += 1
      right -= 1
    elif l[left] == 0 and l[right] != 0:
      # swap the values
      temp = l[left]
      l[left] = l[right]
      l[right] = temp
      
      # advance both pointers
      left += 1
      right -= 1
    else:
      left += 1
      
  return l
      
print(zero_end([ 3, 0, 2, 0, 0, 4, 1, 0,5,0,2,4,5,555,0,304,604,403,403,405,304,0,2,304,0,3,0,0,0,3 ]))


