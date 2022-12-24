class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                j = i+1
                while j < len(nums):
                    if nums[j]!=val:
                        nums[j],nums[i] = nums[i],nums[j]
                        break
                    else:
                        j+=1
        for x in range(output):
            nums.pop()
            