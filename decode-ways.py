class Solution:
    def numDecodings(self, nums: str) -> int:
        def possible(n):
            if n and 0 < int(n) <= 26 and n[0] != "0":
                return True
            return False
        memo = {}
        def dfs(n,arr):
            if n in memo:
                return memo[n]
            if n == len(nums):
                return 1
            val = 0
            x = 0
            y = 0
            if possible(nums[n:n+1]):
                val += dfs(n+1,arr[n:n+1])
            if possible(nums[n:n+2]):
                val +=  dfs(n+2,arr[n:n+2])
            memo[n] = val
            return val
        return dfs(0,nums[:])