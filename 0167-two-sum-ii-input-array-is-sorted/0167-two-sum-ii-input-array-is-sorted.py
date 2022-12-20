class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums)-1
        l = 0
        res = []
        while l < r:
            Sum = nums[l] + nums[r]
            if Sum < target:
                l+=1
            elif Sum > target:
                r-=1
            else:
                return [l+1,r+1]
