class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
        direction = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j):
            visited.add((i,j))
            for x,y in direction:
                if inbound(x+i,y+j) and (x+i,y+j) not in visited and grid[x+i][y+j] == "1":
                    dfs(x+i,y+j)
        visited = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        return ans

            