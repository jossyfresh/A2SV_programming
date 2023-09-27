class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(i,res):
            if i == len(stones):
                return res
            a = abs(dp(i+1,res-stones[i]))
            b = abs(dp(i+1,res+stones[i]))
            return min(a,b)
        return dp(0,0)