class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(i,j,k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True    
            if i < len(s1) and j < len(s2) and k < len(s3) and s1[i] == s3[k] and s2[j] == s3[k]:

                return dp(i+1,j,k+1) or dp(i,j+1,k+1)
            else:
                if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                    return dp(i+1,j,k+1)
                elif j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                    return dp(i,j+1,k+1)
                else:
                    return False
        return dp(0,0,0)
