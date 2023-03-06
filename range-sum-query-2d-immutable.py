class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = []
        l = [0]*(len(matrix[0])+1)
        self.grid.append(l)
        for i in range(len(matrix)):
            Sum = 0
            x = [0]
            for j in range(len(matrix[0])):
                Sum += matrix[i][j]
                x.append(Sum)
            self.grid.append(x)
        for j in range(len(self.grid[0])):
            Sum = 0
            for i in range(len(self.grid)):
                Sum += self.grid[i][j]
                self.grid[i][j] = Sum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        ans = self.grid[row2][col2] - self.grid[row1-1][col2] - self.grid[row2][col1-1] + self.grid[row1-1][col1-1]
        return ans

        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)