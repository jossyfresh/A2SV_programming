class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        x = 1
        for i in nums:
            if i <= 0:
                continue
            else:
                if i == x:
                    x+=1
                else:
                    return x
        return x