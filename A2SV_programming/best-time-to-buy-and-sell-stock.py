class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(p):
           maxProfit  = max(maxProfit,p[r] - p[l])
           if p[r] < p[l]:
               l = r
               r+=1
           else:
               r+=1
               
        return maxProfit
