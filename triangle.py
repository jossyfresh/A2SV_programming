class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        memo = {}
        def dfs(i,j,total):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(nums)-1:
                return total + nums[i][j]
            x = dfs(i+1,j,total)
            y = dfs(i+1,j+1,total)
            val = min(x,y) + nums[i][j]
            memo[(i,j)] = val
            return val
        return dfs(0,0,0)