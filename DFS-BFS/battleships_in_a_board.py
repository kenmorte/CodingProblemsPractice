# https://leetcode.com/problems/battleships-in-a-board/description/

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.visited = set()
        count = 0
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'X' and (r,c) not in self.visited:
                    # traverse through entire battleship at this point, marking each node in battleship as "visited"
                    self.dfs(board, r, c) 
                    count += 1
        return count
        
    def dfs(self, board, r, c):
        if (r,c) in self.visited:
            return
        if r < 0 or r >= len(board):
            return
        if c < 0 or c >= len(board[r]):
            return
        if board[r][c] == '.':
            return 
        self.visited.add((r,c))
        self.dfs(board, r-1, c) # traverse up
        self.dfs(board, r+1, c) # traverse down
        self.dfs(board, r, c-1) # traverse left
        self.dfs(board, r, c+1) # traverse right
