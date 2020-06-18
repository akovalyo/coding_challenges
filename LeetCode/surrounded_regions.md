# Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

```
Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
```

**Explanation:**

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

# Solution

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.row = len(board)
        self.col = 0
        if self.row:
            self.col = len(board[0])
        self.queue = []
        zeros = self.boundary(board)
        while len(self.queue):
            cell = self.queue.pop(0)
            neighbors = self.neighbor(cell)
            for n in neighbors:
                if board[n[0]][n[1]] == 'O' and n not in zeros:
                    self.queue.append(n)
                    zeros.add(n)
        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] == 'O' and (row, col) not in zeros:
                    board[row][col] = 'X'
        
    def boundary(self, board):
        b = set()
        for i in range(self.col):
            if board[0][i] == 'O' and (0, i) not in b:
                b.add((0, i))
                self.queue.append((0, i))
            if board[self.row - 1][i] == 'O' and (self.row - 1, i) not in b:    
                b.add((self.row - 1, i))
                self.queue.append((self.row - 1, i))
        for i in range(self.row):
            if board[i][0] == 'O' and (i, 0) not in b:
                b.add((i, 0))
                self.queue.append((i, 0))
            if board[i][self.col - 1] == 'O' and (i, self.col -1) not in b:
                b.add((i, self.col - 1))
                self.queue.append((i, self.col - 1))
        return b
    
    def neighbor(self, cell):
        n = []
        if cell[0] - 1 >= 0:
            n.append((cell[0] - 1, cell[1]))
        if cell[1] - 1 >= 0:
            n.append((cell[0], cell[1] - 1))
        if cell[0] + 1 < self.row:
            n.append((cell[0] + 1, cell[1]))
        if cell[1] + 1 < self.col:
            n.append((cell[0], cell[1] + 1))
        return n
```