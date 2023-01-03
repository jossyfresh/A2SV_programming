class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        count = 0
        for row in range(len(grid)):
            x = []
            for col in range(len(grid[0])):
                x.append(grid[row][col])
            rows.append(x)
        for col in range(len(grid[0])):
            x = []
            for row in range(len(grid)):
                x.append(grid[row][col])
            cols.append(x)
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == cols[j]:
                    count+=1
        return count
