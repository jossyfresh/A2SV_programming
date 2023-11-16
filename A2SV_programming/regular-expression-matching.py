class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if i >= len(s) or j >= len(p):
                if j == len(p):
                    return i == len(s)
            x = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                res = dp(i, j + 2) or (x and dp(i + 1, j))
            else:
                res = x and  dp(i + 1, j + 1)
            return res
        return dp(0, 0)



       
            

            
            