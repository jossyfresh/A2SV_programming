class Solution:
    def findComplement(self, num: int) -> int:
        t = str(bin(num))
        s = list(t[2:])
        for i in range(len(s)):
            if s[i] == "0":
                s[i] = "1"
            else:
                s[i] = "0"
        st = "".join(s)
        return int(st,2)