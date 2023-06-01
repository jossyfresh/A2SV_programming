class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0] * (n+1)
        if n >= 2:
            memo[0] = 0
            memo[1] = 1
            ans = []
            for i in range(n):
                j = 2 * i
                if 2 <= j <= n:
                    memo[j] = memo[i]
                k = 2 * i + 1
                if 2 <= k <= n:
                    memo[k] = memo[i] + memo[i + 1]
            return max(memo)
        else:
            if n == 1:
                return 1
            else:
                return 0