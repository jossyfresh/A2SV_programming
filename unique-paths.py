class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for j in range(m)]
        finalx = m-1
        finaly = n-1
        moves = [(-1,0),(0,-1)]
        print(memo)
        def inbound(row,col):
            return 0 <= row <= m and 0 <= col <= n
        def dfs(i,j):
            if memo[i][j] != 0:
                return memo[i][j]
            if (i,j) == (0,0):
                return 1
            for x,y in moves:
                if inbound(x+i,y+j):
                    memo[i][j] += dfs(x+i,y+j)
            return memo[i][j]
        return dfs(finalx,finaly)