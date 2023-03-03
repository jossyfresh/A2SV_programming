class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = []
        stack = []
        max_ = 0
        for i in range(len(nums)):
            max_= max(max_,nums[i])
            while stack and nums[stack[-1]] < nums[i]:
                m.append([stack.pop(),nums[i]])
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                m.append([stack.pop(),nums[i]])
        ans = [-1]*len(nums)
        for x in m:
            ans[x[0]] = x[1]
        return ans