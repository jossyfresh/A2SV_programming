class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        char = ""
        max_ = 0
        ans = 0
        r = 0
        l = 0
        while r < len(s):
            char = s[r]
            counter[char] = counter.get(char,0)+1
            max_ = max(counter[char],max_)

            while r - l - max_ + 1 > k:
                counter[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans