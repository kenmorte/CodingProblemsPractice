# https://leetcode.com/problems/flood-fill/description/

class Solution(object):
    def floodFill(self, I, sr, sc, NC):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not I: return []
        V = set()
        self.dfs(I, sr, sc, NC, I[sr][sc], V)
        return I
        
    def dfs(self, I, r, c, NC, CC, V):
        V.add((r,c))
        if self.isValid(I,r-1,c,V,CC): self.dfs(I,r-1,c,NC,CC,V)
        if self.isValid(I,r+1,c,V,CC): self.dfs(I,r+1,c,NC,CC,V)
        if self.isValid(I,r,c-1,V,CC): self.dfs(I,r,c-1,NC,CC,V)
        if self.isValid(I,r,c+1,V,CC): self.dfs(I,r,c+1,NC,CC,V)
        I[r][c] = NC

            
    def isValid(self, I, r, c, V, CC):
        return r >= 0 and r < len(I) and c >= 0 and c < len(I[r]) and (r,c) not in V and I[r][c] == CC
