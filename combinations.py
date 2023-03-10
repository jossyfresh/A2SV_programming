class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        ans = []
        for i in range(1,n+1):
            nums.append(i)
        def backtrack(i,comb):
            if len(comb) == k:
                ans.append(comb[:])
                return 
            if i >= n:
                return 
            backtrack(i+1,comb+[nums[i]])

            backtrack(i+1,comb)
        backtrack(0,[])
        return ans