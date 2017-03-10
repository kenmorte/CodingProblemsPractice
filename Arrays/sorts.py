def quicksort(l):
  if len(l) == 0 or len(l) == 1:
    return l
  
  pivot = l[0]
  less = []
  equal = []
  greater = []
  
  for n in l:
    if n < pivot:
      less.append(n)
    elif n == pivot:
      equal.append(n)
    else:
      greater.append(n)
  
  return quicksort(less) + equal + quicksort(greater)
  
def merge(a,b):
  result = []
  
  a_i = 0
  b_i = 0
  while a_i < len(a) or b_i < len(b):
    if a_i < len(a) and b_i < len(b):
      to_add = min(a[a_i], b[b_i])
      if to_add == a[a_i]:
        a_i += 1
      else:
        b_i += 1
      result.append(to_add)
    
    elif a_i < len(a):
      result.append(a[a_i])
      a_i += 1
    elif b_i < len(b):
      result.append(b[b_i])
      b_i += 1
    
  return result
  
def mergesort(l):
  if len(l) == 0 or len(l) == 1:
    return l
  
  half_index = len(l) // 2
  a = mergesort(l[:half_index])
  b = mergesort(l[half_index:])
  
  return merge(a,b)

  
l = [1,67,3245,6,345,456,324,357,653,783,8,15,1347,2816436,5,7568,58,4,6]
assert quicksort(l) == sorted(l)
assert mergesort(l) == sorted(l)
