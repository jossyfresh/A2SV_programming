class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = maps.get(nums[i],0)+1
        for x in nums:
            if maps[x] < 2:
                return x