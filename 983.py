class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = {0:1,1:7,2:30}
        @cache
        def dp(i):
            if i >= len(days):
                return 0
            res = float("inf")
            for j in range(len(costs)):
                nextday = days[i] + travel[j]
                nextindx = bisect_left(days,nextday)
                res = min(res,dp(nextindx) + costs[j])
            return res
        return dp(0)
                  