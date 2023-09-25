class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        if n == 1:
            return 0
        def dp(i,prev):
            if i >= n:
                if i == n:
                    return 1
                else:
                    return float('inf')
            x = dp(i+prev,prev) + 1
            y = dp(i+prev,i+prev) + 2 
            return min(x,y)
        return dp(1,1)