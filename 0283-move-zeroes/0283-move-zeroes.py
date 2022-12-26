class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        zeros =0
        for r in nums:
            if not r:
                zeros += 1
            if r:
                nums[i] = r
                i+=1
        y = len(nums)-zeros
        for x in range(y,len(nums)):
            nums[x] = 0
        
                