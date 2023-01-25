class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        k = 0
        while r < len(nums):
            if nums[l] == nums[r]:
                nums[r] = 1000
                r+=1
                k+=1
            else:
                l=r
                r+=1
        i = 0
        j = 0
        while j < len(nums):
            if nums[j]!= 1000:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1
        return len(nums)-k
        
        
        
        
            