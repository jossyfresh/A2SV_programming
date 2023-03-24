class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def dfs(i,arr):
            if len(arr) >= 2:
                if tuple(arr) not in ans:
                    ans.add(tuple(arr[:]))
            for j in range(i,len(nums)):
                if nums[j] >= arr[-1]:
                    arr.append(nums[j])
                    dfs(j+1,arr)
                    arr.pop()
        for i in range(len(nums)):
            arr = [nums[i]]
            dfs(i+1,arr)
        return ans