# Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
Example 1:

Input:
11110
11010
11000
00000

Output: 
1

***

Example 2:

Input:
11000
11000
00100
00011

Output: 
3
```

***

# Solution

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = 0
        if self.rows:
            self.cols = len(grid[0])
        self.checked = set()
        self.ingrid = self.buildingrid()
        count = 0
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "1" and (row, col) not in self.checked:
                    count += 1
                    self.dfsearch((row,col))
        return count
    
    def find_neighbours(self, cell):
        neighbours = []
        if (cell[0], cell[1]-1) in self.ingrid and self.grid[cell[0]][cell[1]-1] == "1":
            neighbours.append((cell[0], cell[1]-1))
        if (cell[0], cell[1]+1) in self.ingrid and self.grid[cell[0]][cell[1]+1] == "1":
            neighbours.append((cell[0], cell[1]+1))
        if (cell[0]-1, cell[1]) in self.ingrid and self.grid[cell[0]-1][cell[1]] == "1":
            neighbours.append((cell[0]-1, cell[1]))
        if (cell[0]+1, cell[1]) in self.ingrid and self.grid[cell[0]+1][cell[1]] == "1":
            neighbours.append((cell[0]+1, cell[1]))
        return neighbours
    
    def dfsearch(self, cell):
        self.checked.add(cell)
        neighbours = self.find_neighbours(cell)
        for n in neighbours:
            if self.grid[n[0]][n[1]] == "1" and n not in self.checked:
                self.dfsearch(n)
        
    def buildingrid(self):
        ingrid = set()
        for row in range(self.rows):
            for col in range(self.cols):
                ingrid.add((row,col))
        return ingrid
```
