class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mask = nums[0]
        for num in nums:
            mask = mask & num
        if mask: return 1
        curmask = 2**20 - 1
        res = 0
        for num in nums:
            curmask &= num
            if not curmask:
                res += 1
                curmask = 2**20 - 1
        return res