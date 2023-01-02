class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = []
        cols = []
        len_ = len(grid[0])
        for row in range(len(grid)):
            sums = 0
            for col in range(len_):
                sums+=grid[row][col]
            rows.append(sums)
        for col in range(len(grid[0])):
            sums = 0
            for row in range(len(grid)):
                sums+=grid[row][col]
            cols.append(sums)
        diff = []
        for i in range(len(grid)):
            list = []
            for j in range(len(grid[0])):
                val = (rows[i] + cols[j]) - (len(cols)-rows[i] + len(rows)-cols[j])
                list.append(val)
            diff.append(list)
        
        return diff
        