class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i,a,b):
            if i == len(costs):
                if a == b:
                    return 0
                return float("inf")
            x = dp(i+1,a+1,b) + costs[i][0]
            y = dp(i+1,a,b+1) + costs[i][1]
            return min(x,y)
        return dp(0,0,0)