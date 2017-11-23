# https://leetcode.com/problems/game-of-life/description/

class Solution(object):
    def gameOfLife(self, m):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not m: return
        for i in xrange(len(m)):
            for j in xrange(len(m[i])):
                n = self.checkNeighbors(m, i, j)
                isDeadNow = m[i][j] == 0
                isDeadLater = (not isDeadNow and n < 2) or (not isDeadNow and n > 3) or (isDeadNow and n != 3)
                m[i][j] = 0 if isDeadNow and isDeadLater else 1 if not isDeadNow and not isDeadLater else 2 if isDeadNow and not isDeadLater else 3
                
        for i in xrange(len(m)):
            for j in xrange(len(m[i])):
                m[i][j] = 0 if m[i][j] == 3 or m[i][j] == 0 else 1
        
    def checkNeighbors(self, m,i,j):
        res = 0
        up_valid, left_valid, down_valid, right_valid = i > 0, j > 0, i < len(m)-1, j < len(m[0])-1
        if up_valid:
            res += 1 if self.isAlive(m[i-1][j]) else 0
            if left_valid: res += 1 if self.isAlive(m[i-1][j-1]) else 0
            if right_valid: res += 1 if self.isAlive(m[i-1][j+1]) else 0
        if down_valid:
            res += 1 if self.isAlive(m[i+1][j]) else 0
            if left_valid: res += 1 if self.isAlive(m[i+1][j-1]) else 0
            if right_valid: res += 1 if self.isAlive(m[i+1][j+1]) else 0
        if left_valid: res += 1 if self.isAlive(m[i][j-1]) else 0
        if right_valid: res += 1 if self.isAlive(m[i][j+1]) else 0
        return res
    
    def isAlive(self, cell):
        return cell == 1 or cell == 3
