class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] == nums[left]:
                nums[right] = 0
                nums[left] *= 2
            left+=1
            right+=1
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i+1
                while j < len(nums):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                    j+=1
            i+=1
        return nums
                
        