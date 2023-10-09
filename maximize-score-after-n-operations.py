class Solution:
    def maxScore(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        arr = list(itertools.combinations(nums,2))
        for i in range(len(arr)):
            arr[i] = (gcd(arr[i][0][0],arr[i][1][0]),arr[i][0][1],arr[i][1][1])
        arr.sort()
        visit = set()
        ans = [0]
        def back(i,op,score):
            if op == 0:
                ans[0] = max(ans[0],score)
            elif i >= 0:
                gcd,ind,jnd = arr[i]
                if gcd == 1:
                    ans[0] = max(ans[0],(op + 1) * op // 2 + score)
                    return 
                if ind not in visit and jnd not in visit:
                    visit.add(ind)
                    visit.add(jnd)
                    back(i-1,op - 1,score + (op * (gcd)))
                    visit.remove(ind)
                    visit.remove(jnd)
                back(i-1,op,score) 
        back(len(arr)-1,len(nums) // 2,0)
        return ans[0]