class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = 0
        Bool = False
        for i in range(1,len(matrix)):
            if target < matrix[i][0]:
                x = i-1
                break
            elif target >= matrix[i][0]:
                x = i
        for i in range(len(matrix[x])):
            if target == matrix[x][i]:
                return True
                break
        return Bool