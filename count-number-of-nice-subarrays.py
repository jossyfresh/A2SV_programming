class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        print(nums)
        pre = {0:1}
        Sum = 0
        ans = 0
        for val in nums:
            Sum+=val
            x = Sum-k
            ans += pre.get(x,0)
            pre[Sum] = pre.get(Sum,0) + 1
        return ans