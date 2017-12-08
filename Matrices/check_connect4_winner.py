# NOTE: This was asked at my Redfin phone interview 12/7/2017

'''
Connect 4

| - / \ 

o o o _ o o o
# o or an x 
# o o o o

x,y - coords of the last placed piece
m x n - board
boolean checkWinner(board, x, y) 


# Edge cases
#  Checking at the borders: top left corner, top right corner, top, bottom, bottom corners
#  Position tests: middle, middle top left
#  Board matrix -> empty board, board with 1 row, 1 col, square board (large size, small size), rectangular boards (m>n, n>m)
'''

def checkWinner(board, x, y):
  countLeft = checkDirection(board, x, y, 'L')  
  countRight = checkDirection(board, x, y, 'R')
  
  countUp = checkDirection(board, x, y, 'U')  
  countDown = checkDirection(board, x, y, 'D')  
  
  countUpLeft = checkDirection(board, x, y, 'UL')  
  countDownRight = checkDirection(board, x, y, 'DR')  
  
  countUpRight = checkDirection(board, x, y, 'UR')
  countDownLeft = checkDirection(board, x, y, 'DL')  
  
  return countUp + countDown >= 3 or countLeft + countRight >= 3 or countUpLeft + countDownRight >= 3 or countUpRight + countDownLeft >= 3



# Directions = U, D, L, R, UL, UR, DL, DR
# x is affected if U, D is inside direction
def checkDirection(board, x, y, direction): # (int, color)
  dx = -1 if 'U' in direction else 1 if 'D' in direction else 0
  dy = -1 if 'L' in direction else 1 if 'R' in direction else 0
  
  count = 0 
  color = board[x][y]
  
  x += dx
  y += dy
  
  while x >= 0 and x < len(board) and y >= 0 and y < len(board[x]):
    if board[x][y] == color:
      count += 1
      x += dx
      y += dy
    else:
      break
    if count >= 3: break
  return count


