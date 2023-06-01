class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        dp = [float(inf)] * (len(nums)+1)

        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
            else:
                dp[i] = min(dp[i-1],dp[i-2]) + nums[i]
        return min(dp[len(nums)-1],dp[len(nums)-2])