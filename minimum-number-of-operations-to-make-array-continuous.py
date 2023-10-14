class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)-1
        num = list(set(nums))
        num.sort()
        ans = float('inf')
        for i in range(len(num)):
            val = num[i] + n
            right = bisect.bisect_right(num,val)
            res = n+1 - (right - i)
            ans = min(ans,res)
        return ans