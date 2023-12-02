class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i,j):
            if i >= len(word1) or j >= len(word2):
                if i == len(word1) and j == len(word2): 
                   return 0
                elif j == len(word2):
                    return len(word1) - i
                else:
                    return len(word2) - j
            if word1[i] == word2[j]:
                return dp(i+1,j+1)
            return min(dp(i+1,j+1) + 1,dp(i,j+1) + 1,dp(i+1,j) + 1)
        return dp(0,0)

