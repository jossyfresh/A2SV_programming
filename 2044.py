class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_ = 0
        for i in range(len(nums)):
            max_ = max_ | nums[i]
        ans = 0
        @cache
        def dp(i,count):
            if i == len(nums):
                if count == max_:
                    return 1
                return 0
            return dp(i+1,count | nums[i]) + dp(i+1,count)
        return dp(0,0)
