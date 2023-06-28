class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        Sum = 0
        ans = 0
        for i in range(len(nums)):
            Sum += nums[i]
            ans = max(ans,Sum/(i+1))
        return math.ceil(ans)