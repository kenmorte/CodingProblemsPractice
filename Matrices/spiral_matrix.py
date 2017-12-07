# https://leetcode.com/problems/spiral-matrix/description/

class Solution(object):
    def spiralOrder(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not M: return []
        r,c,curr = 0,0,'R'
        V, res = set(), []
        while self.isValid(r,c,M,V):
            res.append(M[r][c])
            V.add((r,c))
            if curr == 'R':
                if self.isValid(r,c+1,M,V): c += 1
                else: r,curr = r+1,'D'
            elif curr == 'D':
                if self.isValid(r+1,c,M,V): r += 1
                else: c,curr = c-1,'L'
            elif curr == 'L':
                if self.isValid(r,c-1,M,V): c -= 1
                else: r,curr = r-1,'U'
            else:
                if self.isValid(r-1,c,M,V): r -= 1
                else: c,curr = c+1,'R'
        return res
        
    def isValid(self, r, c, M, V):
        return r >= 0 and r < len(M) and c >= 0 and c < len(M[r]) and (r,c) not in V
