class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        n = len(s)-1
        if len(s) == 1:
            return 1
        @cache
        def dp(i,j):
            if i >= j:
                if i == j:
                    return 1
                return 0
            if s[i] == s[j]:
                x = dp(i+1,j-1) + 2
            else:
                x = max(dp(i+1,j),dp(i,j-1))
            return x
        return dp(0,n)