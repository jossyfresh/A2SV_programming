class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(k,arr):
            ans.append(arr)
            if k >= len(nums):
                return 
            for i in range(k,len(nums)):
                backtrack(i+1,arr+[nums[i]])
        backtrack(0,[])
        return ans