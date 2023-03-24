class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_ = 0
        def dfs(i,s):
            nonlocal max_
            if len(s) == len(set(s)):
                max_= max(len(set(s)),max_)
            if len(s) > len(set(s)):
                return 
            print(s)
            for j in range(i,len(arr)):
                s += arr[j]
                dfs(j+1,s)
                l = len(s) - len(arr[j])
                s = s[:l]
        for i in range(len(arr)):
            s = arr[i]
            if len(s) == len(set(s)):
                dfs(i+1,s)
        return max_