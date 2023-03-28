class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            if x not in nums:
                return x