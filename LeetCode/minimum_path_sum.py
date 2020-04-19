class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = 0
        if rows:
            cols = len(grid[0])
        cp_grid = [[0 for col in range(cols)] for row in range(rows)]
        cp_grid[0][0] = grid[0][0]
        
        for col in range(1, cols):
            cp_grid[0][col] = cp_grid[0][col-1] + grid[0][col]   
        for row in range(1, rows):
            cp_grid[row][0] = cp_grid[row-1][0] + grid[row][0]  
        
        for row in range(1, rows):
            for col in range(1, cols):
                cp_grid[row][col] = min((grid[row][col] + cp_grid[row-1][col]), (grid[row][col] + cp_grid[row][col-1]))
        
        return cp_grid[rows-1][cols-1]