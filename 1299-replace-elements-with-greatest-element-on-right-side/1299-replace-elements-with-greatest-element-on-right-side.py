class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        d = {}
        ans = []
        x = 0
        for i in range(len(arr)):
            d[arr[i]] = i
        dic = sorted(d,reverse=True)
        for i in range(len(dic)):
            for j in range(x,d[dic[i]]):
                ans.append(dic[i])
                x+=1
        ans.append(-1)
        
        return ans