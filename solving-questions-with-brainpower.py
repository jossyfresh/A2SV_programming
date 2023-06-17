class Solution:
    def mostPoints(self, nums: List[List[int]]) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n >= len(nums):
                return 0
            nxt = (nums[n][1])+1
            x = dfs(n+nxt) + nums[n][0]
            y = dfs(n+1)
            val = max(x,y)
            memo[n] = val
            return val
        return dfs(0)