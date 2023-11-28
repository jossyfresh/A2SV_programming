class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
        direction = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j):
            visited.add((i,j))
            total.add((i,j))
            for x,y in direction:
                if inbound(x+i,y+j) and (x+i,y+j) not in total and grid[x+i][y+j] == 1:
                    dfs(x+i,y+j)
        
        ans = 0
        total = set()
        for i in range(n):
            for j in range(m):
                if (i,j) not in total and grid[i][j] == 1:
                    visited = set()
                    dfs(i,j)
                    ans = max(ans,len(visited))
        return ans
        
        