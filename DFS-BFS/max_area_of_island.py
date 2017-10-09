# https://leetcode.com/problems/max-area-of-island/description/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.visited = set()
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]:
                    result = max(result, self.visit(grid, (r, c)))
        return result
        
    def visit(self, grid, position):
        r, c = position
        if not self.positionIsValid(grid, r, c):
            return 0
        if not grid[r][c]:
            return 0
        if (r, c) in self.visited:
            return 0
        self.visited.add((r,c))
        return 1 + self.visit(grid, (r-1,c)) + self.visit(grid, (r, c-1)) + self.visit(grid, (r+1, c)) + self.visit(grid, (r, c+1)) 
        
        
    def positionIsValid(self, grid, r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])
