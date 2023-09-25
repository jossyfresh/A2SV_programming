class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        nums = list(zip(ages,scores))
        nums.sort()
        dp = [0]*len(nums)
        for i in range(len(nums)):
            val = nums[i][1]
            dp[i] = val
            for j in range(i):
                if val >= nums[j][1]:
                    dp[i] = max(dp[i],dp[j]+val)
        return max(dp)