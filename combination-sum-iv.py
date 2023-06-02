class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 1
            if target < 0:
                return 0
            val = 0
            for i in range(len(nums)):
                val += dfs(target-nums[i])
            memo[target] = val
            return val
        return dfs(target)