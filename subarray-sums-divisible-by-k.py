class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = {0:1}
        Sum = 0
        ans = 0
        for val in nums:
            Sum += val
            x = Sum%k
            ans += pre.get(x,0)
            pre[x] = pre.get(x,0) + 1
        return ans