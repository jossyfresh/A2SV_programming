class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        k = m-1
        r = 1
        while r < m+n:
            i = k
            j = l
            x = matrix[i][j]
            while i<=m-1 and j<=n-1:
                if matrix[i][j] != x:
                    return False
                i+=1
                j+=1
            if k == 0:
                l+=1
            else:
                k-=1
            r+=1
        return True