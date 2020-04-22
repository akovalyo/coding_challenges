class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        rows = dim[0]
        col = dim[1] - 1
        row = 0
        one = 0
        while col >= 0 and row < rows:
            value = binaryMatrix.get(row, col)
            if value == 0:
                row += 1
                col += 1
            else:
                one = 1
            col -= 1
            continue
        if col < 0:
            return 0
        elif row >= rows and one == 0:
            return -1
        else:
            return col + 1
        