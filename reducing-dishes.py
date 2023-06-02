class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums.sort()
        memo = {}
        def dfs(n,c):
            if (n,c) in memo:
                return memo[(n,c)]
            if n == len(nums):
                return 0
            x = dfs(n+1,c+1) + (nums[n]*c)
            y = dfs(n+1,c)
            val = max(x,y) 
            memo[(n,c)] = val
            return val
        return dfs(0,1)