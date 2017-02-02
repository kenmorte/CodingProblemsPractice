# Remove duplicates from a list


# Can use dictionaries, require O(n) time but O(n) space
# Preserves ordering!
def remove_dups(l: [int]) -> [int]:
  values = {}
  result = list()
  for n in l:
    if n not in values:
      values[n] = True
      result.append(n)
  return result
  
# Can use sets, which require O(n) time and O(n) space
# Does not preserve ordering!
def remove_dups1(l: [int]) -> [int]:
  return list(set(l))
  

  
print(remove_dups1([1,2,3,1,2,3,1,3,32,2,3,4,1,4,1,6,78,9,5,5,3,5,6]))
