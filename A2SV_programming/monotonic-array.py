class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        new = []
        for i in range(len(nums)-1):
            new.append(nums[i] - nums[i+1])
        n = 0
        p = 0
        for i in range(len(new)):
            if new[i] > 0:
                p = 1
            if new[i] < 0:
                n = 1
        if n and p:
            return False
        return True
 
        