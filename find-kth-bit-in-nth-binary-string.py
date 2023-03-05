class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(stri):
            for i in range(len(stri)):
                if stri[i] == "0":
                    stri[i] = "1"
                else:
                    stri[i] = "0"
            return stri
        def recur(n):
            if n == 1:
                return ["0"]
            new = recur(n-1)
            return new + ["1"] + invert(new)[::-1]
        string = recur(n)
        return string[k-1]