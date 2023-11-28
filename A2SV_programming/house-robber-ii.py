class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp1 = [0] * n
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        ans1 = dp1[n-2]
        dp2 = [0] * n
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        ans2 = dp2[n-1]
        return max(ans1,ans2)


        