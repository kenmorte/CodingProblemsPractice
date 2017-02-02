hex = {
  10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'
  }

def toBaseRepr(n: str):
  return [int(i) for i in list(n)]

def toHex(d: int):
  if d > 9:
    return hex[d]
  return str(d)

def base6to10(n: [int]):
  index = 0
  result = 0
  for i in reversed(n): # iterate through the base-6 left-to-right
    result += i * (6 ** index)
    index += 1
  return result
 
def base10to16(n: int):
  if n == 0:
    return 0
  result = []
  while (n // 16 != 0):
    result.append(toHex(n%16))
    n = n // 16
  result.append(toHex(n%16))
  return ''.join(list(reversed(result)))

def base6to16(n: str):
  # n is a base 6 number
  base10 = base6to10(toBaseRepr(n))
  return base10to16(base10)
