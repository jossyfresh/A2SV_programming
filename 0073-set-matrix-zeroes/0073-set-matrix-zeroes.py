class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero.append([i,j])
        for k,l in zero:
            for i in range(m):
                matrix[i][l] = 0
            for j in range(n):
                matrix[k][j] = 0
    
