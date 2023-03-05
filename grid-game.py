class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pre = [[0],[0]]
        Sum = 0
        Sum1 = 0
        for i in range(2):
            Sum = 0
            for j in range(len(grid[i])):
                Sum += grid[i][j]
                pre[i].append(Sum)
        max_ = inf
        i = 0
        print(pre)
        for j in range(len(grid[0])):
            pre[0][-1] -= grid[0][j]
            x = max(pre[0][-1],pre[1][i])
            max_ = min(max_,x)
            i+=1
        return max_