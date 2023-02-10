class Solution:
    def reverseWords(self, s: str) -> str:
        ans = list(map(str,s.split(" ")))
        new = []
        for i in range(len(ans)-1,-1,-1):
            if ans[i] != "":
                new.append(ans[i])
        return " ".join(new)
            