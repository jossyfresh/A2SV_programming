class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r = 11
        l = 1
        m = {s[:10] : 1}
        while r < len(s)+1:
            m[s[l:r]] = m.get(s[l:r],0) + 1
            r +=1
            l += 1
        ans = []
        for x in m:
            if m[x] > 1:
                ans.append(x)
        return ans
