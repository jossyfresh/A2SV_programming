class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rotate(nums,l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        k = k % len(nums)
        if len(nums) > 1:
            rotate(nums,0,len(nums)-1)
            rotate(nums,0,k-1)
            rotate(nums,k,len(nums)-1)