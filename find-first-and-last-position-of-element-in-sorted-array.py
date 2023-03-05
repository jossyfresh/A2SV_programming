class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            x = bisect_left(nums,target)
            y = bisect_right(nums,target)
            if nums[y-1] == target:
                return [x,y-1]
        return [-1,-1]