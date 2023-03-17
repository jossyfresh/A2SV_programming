class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        x = -((10**9)+1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < x:
                return True
            while stack and stack[-1] < nums[i]:
                x = stack.pop()
            stack.append(nums[i])
        return False