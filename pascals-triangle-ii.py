class Solution:
    def getRow(self, r: int) -> List[int]:
        if r == 0:
            return [1] 
        else:
            x = self.getRow(r-1)
            ans = [1]
            for i in range(len(x)-1):
                ans.append(x[i]+x[i+1])
            ans.append(1)
            return ans