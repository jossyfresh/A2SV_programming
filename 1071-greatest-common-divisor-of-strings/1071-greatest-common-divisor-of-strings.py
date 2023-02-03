class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        ans = ""
        k = math.gcd(len(s),len(t))
        l = 0
        r = 0
        h = 0
        while l < len(s) and r < len(t) and h < k:
            if s[l] == t[r]:
                ans+=s[l]
                r+=1
                l+=1
                h+=1
            else:
                return ""
        l = 0
        r = 0
        while l < len(s):
            if ans == s[l:l+k]:
                l = l+k
            else:
                return ""
        while r < len(t):
            if ans == t[r:r+k]:
                r = r+k
            else:
                return ""
        return ans