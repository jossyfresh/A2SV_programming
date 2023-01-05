class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        ans = []
        word = ""
        max_ = len(s[0])
        for x in s:
            max_ = max(max_,len(x))
        for i in range(max_):
            word = ""
            for j in range(len(s)):
                if i < len(s[j]):
                    word+=s[j][i]
                else:
                    word+=" "
            new = word.rstrip(" ")
            ans.append(new)
        return ans