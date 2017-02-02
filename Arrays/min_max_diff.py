# Find minimum and maximum difference within a list


# Get the max and max elements, subtract those 2 --> max difference
# Sort the list, traverse through to find min difference
#   O(nlogn) time complexity from sorting
#   O(1) space complexity

def max_diff(l: [int]) -> int:
  if len(l) == 0:
    raise Exception
  max = l[0]
  min = l[0]
  for n in l:
    if n > max:
      max = n
    elif n < min:
      min = n
  return max - min
  
def min_diff(l: [int]) -> int:
  if len(l) == 0 or len(l) == 1:
    return 0
  
  l.sort()
  result = abs(l[0]-l[1])
  for i in range(1,len(l)):
    if abs(l[i]-l[i-1]) < result:
      result = abs(l[i]-l[i-1])
  return result

def min_max_diff(l: [int]) -> (int,int):
  return (min_diff(l), max_diff(l))

print(min_max_diff([1,234,3,5,34,567,8,58,5,8,6,8,78,678,4,6,5,653,687,3,6,6,67,68,345,3]))

