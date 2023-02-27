class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0]*(len(nums)+1)
        Sum = 0
        for x in requests:
            pre[x[0]] += 1
            pre[x[1]+1] -= 1
        for i in range(len(pre)):
            Sum+=pre[i]
            pre[i] = Sum
        pre = pre[:-1]
        nums.sort()
        m = {}
        for i,x in enumerate(pre):
            m[i] = x
        sm = dict(sorted(m.items(),key = lambda x:x[1], reverse = True))
        i = 1
        for key in sm:
            pre[key] = nums[-i] 
            i+=1
        Sum = 0
        for i in range(len(pre)):
            Sum += pre[i]
            pre[i] = Sum
        pre.insert(0,0)
        pre.append(0) 
        ans = 0
        for x in requests:
            val = pre[x[1]+1] - pre[x[0]]
            ans+=val
        return ans%((10**9)+7)