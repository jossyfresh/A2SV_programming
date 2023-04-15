class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            cp = nums[i] -1
            if cp < len(nums) and cp >= 0 and nums[cp] != nums[i]:
                nums[i],nums[cp] = nums[cp],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]