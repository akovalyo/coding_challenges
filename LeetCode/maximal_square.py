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