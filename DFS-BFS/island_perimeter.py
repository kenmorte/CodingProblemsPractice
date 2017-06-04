# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        self.number_of_rows = len(grid)
        self.number_of_columns = len(grid[0])
        self.visited = set()
        self.perimeter = 0
        
        self.dfs(grid, 0, 0)
        
        # count the bottom borders of the bottom islands
        for j in range(self.number_of_columns):
            if grid[self.number_of_rows-1][j]:
                self.perimeter += 1
        
        # count the right borders of the rightmost islands
        for i in range(self.number_of_rows):
            if grid[i][self.number_of_columns-1]:
                self.perimeter += 1
                
        return self.perimeter
        
    
    def dfs(self, grid, i, j):
        if i >= self.number_of_rows or j >= self.number_of_columns:
            return
        if (i,j) in self.visited:
            return
        
        self.visited.add((i,j)) # add node to our set of visited nodes
        node = grid[i][j]
        original_perimeter = self.perimeter
        
        if not node:    # current node is water
            if j-1 >= 0 and grid[i][j-1]:    # node to your left is land
                self.perimeter += 1
            if i-1 >= 0 and grid[i-1][j]:    # node to your top is land
                self.perimeter += 1
                
        else:   # current node is land
            if j-1 < 0 or not grid[i][j-1]:    # node to your left is water
                self.perimeter += 1
            if i-1 < 0 or not grid[i-1][j]:    # node to your top is water
                self.perimeter += 1
        
        # print 'At island[', i, '][', j, '], counted ', self.perimeter - original_perimeter, ' sides!'
        
        self.dfs(grid, i, j+1)  # dfs to the right
        self.dfs(grid, i+1, j)  # dfs to the bottom
            
        
        # DFS?
        # Remeber to keep track of visited nodes!
        # Start at one node --> check left and top
        #   If you're water
        #       If water is on your left --> dont do anything
        #       Else --> perimeter++
        #
        #       If water is on your top --> dont do anything
        #       Else --> perimeter++
        #   If you're land
        #       If water is on your left --> perimeter++
        #       Else --> dont do anything
        #       
        #       If water is on your top --> perimeter++
        #       Else --> dont do anything
        #   DFS to the right
        #   DFS to the bottom
        # At the very end, count the bottom borders of the rectangle
