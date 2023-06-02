class Solution:
    def longestSubsequence(self, nums: List[int], diff: int) -> int:
        dp = defaultdict(int)
        for i in range(len(nums)):
            val = (nums[i] - diff)
            dp[nums[i]] = dp[val] + 1
        return max(dp.values())