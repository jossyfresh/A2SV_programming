class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = -inf
        r = 0
        l = 0
        Sum = 0
        avg = 0
        i = 0
        while r < len(nums):
            if i == k:
                print(l)
                avg = Sum/k
                max_ = max(max_,avg)
                Sum-=nums[l]
                Sum+=nums[r]
                l+=1
                r+=1
            else:
                Sum+=nums[r]
                r+=1
                i+=1
        max_ = max(Sum/k,max_)
        return max_