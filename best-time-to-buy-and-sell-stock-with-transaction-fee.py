class Solution:
    def maxProfit(self, nums: List[int], fee: int) -> int:
        memo = {}
        def dfs(n,buy):
            if (n,buy) in memo:
                return memo[(n,buy)]
            if n == len(nums):
                return 0
            if buy:
                val = max(dfs(n+1,False)- nums[n],dfs(n+1,True))
            else:
                val = max(dfs(n+1,True) + nums[n] - fee,dfs(n+1,False))
            memo[(n,buy)] = val
            return val
        return dfs(0,True)