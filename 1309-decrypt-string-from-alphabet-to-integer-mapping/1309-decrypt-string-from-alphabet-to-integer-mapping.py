class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict = {}
        output=""
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        l = 0
        for i in range(1,27):
            if i>9:
                i = str(i)+"#"
                dict[i] = alphabets[l]
                l+=1
            else:
                i = str(i)
                dict[i] = alphabets[l]
                l += 1
        l = 0
        while l<len(s):
            if l+2<len(s) and s[l+2] == "#":
                output+=str(dict[s[l:l+3]])
                l+=3
            else:
                output+=str(dict[s[l]])
                l+=1
        return output