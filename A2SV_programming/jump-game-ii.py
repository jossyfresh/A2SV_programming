class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        nextr = 0
        jump  = 0
        while right < len(nums)-1:
            i = left
            r = right
            while i <= r:
                nextr = max(nextr,i+nums[i])
                i+=1
            left = right+1
            right = nextr
            nextr = 0
            jump+=1
        return jump
            