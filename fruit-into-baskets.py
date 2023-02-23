class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        b1 = {}
        r = 0
        max_ = 0
        l = 0
        while r < len(nums):
            if len(b1) <= 2:
                b1[nums[r]] = b1.get(nums[r],0)+1
                max_ = max(max_,r-l)
                r+=1
            while len(b1) > 2:
                b1[nums[l]]-=1
                if b1[nums[l]] == 0:
                    b1.pop(nums[l])
                l+=1 
        max_ = max(max_,r-l) 
        return max_