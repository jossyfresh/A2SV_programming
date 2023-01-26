class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1
        count = 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] > k:
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                count+=1
                l+=1
                r-=1
        return count