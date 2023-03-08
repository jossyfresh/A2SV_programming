class Solution:
    def hIndex(self, nums: List[int]) -> int:
        n = len(nums)
        r = len(nums)-1
        l = 0
        max_ = 0
        if len(nums) == 1:
            if nums[0] != 0:
                return 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= n-mid:
                r = mid -1
                max_ = max(max_,n-mid)
            else:
                l = mid +1
        return max_