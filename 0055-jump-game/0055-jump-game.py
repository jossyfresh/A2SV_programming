class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        jump = 1
        i = len(nums)-2
        while i >= 0:
            if nums[i] >= jump:
                last-=jump
                jump = 1
            else:
                jump+=1
            i-=1
        if last==0:
            return True
        else:
            return False