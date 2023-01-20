class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        new = [0]*size
        for i in range(size):
            for j in range(size):
                if nums[i] > nums[j]:
                        new[i]+=1
        return new