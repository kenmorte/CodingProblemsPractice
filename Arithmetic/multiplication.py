# Write a function which multiples 2 integers without using the multiply operator.  
# Continually add a number x times using a for/while loop
#   - Suggestion: for efficiency, use dynamic programming
#     - Keeping a table of computed values for future operations, kind 
#       of like a times table


def simple_multiplication(a,b):
  result = 0
  neg_flag = (a < 0 and b > 0) or (a > 0 and b < 0)
  
  a = abs(a); b = abs(b)
  while b != 0:
    result += a
    b -= 1
  return result if not neg_flag else -result
  
assert simple_multiplication(1,0) == 0
assert simple_multiplication(1,1) == 1
assert simple_multiplication(1,2) == 2
assert simple_multiplication(1,-1) == -1
assert simple_multiplication(0,1) == 0
assert simple_multiplication(-1,1) == -1
assert simple_multiplication(-1, 2) == -2
assert simple_multiplication(10,10) == 100
assert simple_multiplication(432,33) == 432*33

# Dynamic programming solution assuming max parameter = 100
#   We have a 100x100 times table
times_table = [[None for i in range(101)] for i in range(101)]
def better_multiplication(a,b):
  if times_table[a][b] is not None:
    return times_table[a][b]
  if times_table[b][a] is not None:
    return times_table[b][a]
    
  if a == 0 or b == 0:
    times_table[a][b] = 0
    times_table[b][a] = 0
    return 0
    
  times_table[a][b] = times_table[b][a] = a + better_multiplication(a,b-1)
  return times_table[a][b]
  
assert better_multiplication(1,0) == 0
assert better_multiplication(1,1) == 1
assert better_multiplication(1,2) == 2
assert better_multiplication(5,5) == 25
assert better_multiplication(0,1) == 0
assert better_multiplication(-1,1) == -1
assert better_multiplication(-1, 2) == -2
assert better_multiplication(10,10) == 100
assert better_multiplication(10,100) == 1000
assert better_multiplication(100,100) == 100*100
assert better_multiplication(97,64) == 97*64


