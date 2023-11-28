class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def inbound(row, col):
            return (0 <= row < m and 0 <= col < n)
        direction = [(0, 1), (1, 0),(0, -1), (-1, 0)]
        visited = set()
        def dfs(i,j):
            board[i][j] = "P"
            for x,y in direction:
                newi = x + i
                newj = y + j
                if inbound(newi,newj) and board[newi][newj] == "O":
                    dfs(newi,newj)
        l = 0
        a = 0
        b = 0
        for i in range(4):
            while inbound(a,b):
                if (a,b) not in visited and board[a][b] == "O":
                    visited.add((a,b))
                    dfs(a,b)
                a += direction[l][0]
                b += direction[l][1]
            a -= direction[l][0]
            b -= direction[l][1]
            l += 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == "P":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

            
