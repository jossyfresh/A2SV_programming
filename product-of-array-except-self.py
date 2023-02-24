class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        product = 1
        for x in nums:
            product*=x
            prefix.append(product)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product*=nums[i]
            postfix.append(product)
        print(prefix)
        print(postfix)
        ans = []
        l = 0
        r = len(postfix)-1
        while l < len(nums):
            x = prefix[l] * postfix[r-1]
            l+=1
            r-=1
            ans.append(x)
        return ans