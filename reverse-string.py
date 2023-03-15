class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = []
        for i in range(len(s)-1,-1,-1):
            x.append(s[i])
        for i in range(len(x)):
            s[i] = x[i]