class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        r = 0
        l = 0
        max_ = 0
        while r < len(s):
            while s[r] in x:
                x.remove(s[l])
                l+=1
            x.add(s[r])
            r+=1
            max_ = max(max_,r-l)
        return max_