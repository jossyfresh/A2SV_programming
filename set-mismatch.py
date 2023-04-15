class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            cp = nums[i] -1
            if cp < len(nums) and cp >= 0 and nums[cp] != nums[i]:
                nums[i],nums[cp] = nums[cp],nums[i]
            else:
                i += 1
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
                ans.append(i+1)
        return ans