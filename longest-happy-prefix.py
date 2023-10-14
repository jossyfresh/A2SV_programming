class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0]*len(s)
        lpis = [0]*len(s)
        j = 0
        i = 1
        ans = ''
        while i < len(s):
            if s[i] == s[j]:
                lps[i] = j + 1
                lpis[i] = [i]
                i += 1
                j += 1     
            elif j > 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
        if len(ans) < lps[i-1]:
                ans = s[i-lps[i-1]:i+1]
        return ans