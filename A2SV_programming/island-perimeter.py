class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        land = set()
        ans = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def water(row,col):
            return ( 0 <= row < len(grid) and 0 <= col < len(grid[0])) and (grid[row][col] == 0)
        def dfs(grid, visited, row, col):
            nonlocal ans
            visited.add((row,col))
            if grid[row][col] == 1 and (row,col) not in land:
                land.add((row,col))
                for row_change,col_change in directions:
                    x = row + row_change
                    y = col + col_change
                    if not inbound(x,y) or water(x,y):
                        ans += 1
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
 
                if inbound(new_row, new_col) and (new_row,new_col) not in visited:
                    if grid[new_row][new_col] == 1 and (new_row,new_col) not in land:
                        land.add((new_row,new_col))
                        for row_change,col_change in directions:
                            x = new_row + row_change
                            y = new_col + col_change
                            if not inbound(x,y) or water(x,y):
                                ans += 1
                    dfs(grid, visited, new_row, new_col)
        dfs(grid,visited,0,0)
        return ans

