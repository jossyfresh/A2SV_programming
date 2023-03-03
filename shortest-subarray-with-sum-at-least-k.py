class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        Sum = 0
        for i in range(len(nums)):
            Sum+=nums[i]
            pre.append(Sum)
        print(pre)
        dq = deque()
        ans = len(nums)+1
        for i in range(len(pre)):
            while dq and pre[dq[-1]] >= pre[i]:
                dq.pop()
            while dq and pre[i] >= pre[dq[0]] + k:
                ans = min(ans,i-dq.popleft())
            dq.append(i)

        if ans < len(nums)+1:
            return ans
        else:
            return -1