# Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

```
Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

***

# Solution

```python
class Solution:
    def minThreeNeighbors(self, answer_matr, row, col):
        return min(answer_matr[row][col-1], 
                   answer_matr[row-1][col-1], 
                   answer_matr[row-1][col])
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width = 0
        height = 0
        maxx = 0
        if matrix:
            width = len(matrix[0])
            height = len(matrix)
        answer_matr = [[0 for col in range(width + 1)] for row in range(height +1)]
        for row in range(height):
            for col in range(width):
                if matrix[row][col] == "0":
                    continue
                else:    
                    summ = int(matrix[row][col]) + self.minThreeNeighbors(answer_matr, row+1, col+1)
                answer_matr[row+1][col+1] = summ
                if maxx < summ:
                    maxx = summ
        return maxx * maxx 
```
