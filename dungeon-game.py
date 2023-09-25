class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        finali = n-1
        finalj = m-1
        for i in range(n):
            for j in range(m):
                dungeon[i][j] *= -(1)
        def inbound(i,j):
            return 0 <= i < n and 0 <= j < m
        print(inbound(0,1))
        memo = {}
        def dp(i,j):
            if not inbound(i,j):
                return float('inf')
            if i == finali and j == finalj:
                return max(1,1+dungeon[i][j])
            if (i,j) in memo:
                return memo[(i,j)]
            x = max(1,dp(i,j+1) + dungeon[i][j])
            y = max(1,dp(i+1,j) + dungeon[i][j])
            memo[(i,j)] = min(x,y)
            return min(x,y)
        return dp(0,0)