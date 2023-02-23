class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum = 0
        min_ = inf
        r = 0
        l = 0
        while True:
            if Sum >= target:
                min_ = min(r-l,min_)
                Sum-=nums[l]
                l+=1
            else:
                if r < len(nums):
                    Sum+=nums[r]
                r+=1
            if r > len(nums):
                break
          
        if min_ != inf:
            return min_ 
        else:
            return 0