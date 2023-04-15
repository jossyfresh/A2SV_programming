class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(len(grid)-2)]
        k = 0
        for i in range(len(grid)-2):
            l = 0
            while l < len(grid[i])-2:
                res = 0
                for j in range(i,i+3):
                    res = max(res,max(grid[j][l:l+3]))
                l+=1
                if len(ans[k]) == len(ans):
                    k += 1
                ans[k].append(res)
        return ans