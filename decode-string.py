class Solution:
    def decodeString(self, s: str) -> str:
        i =  0
        r = 0
        stack = []
        new = []
        while i < len(s):
            if s[i] == "]":
                r = i-1
                le = []
                while stack[-1] != "[":
                    le.append(stack.pop())
                stack.pop()
                n = ""
                while stack and stack[-1].isnumeric():
                    n+=stack.pop()
                n = list(n)
                n.reverse()
                n = "".join(n)
                new = int(n) * le 
                new.reverse()
                stack+=new
            else:
                stack.append(s[i])
            i+=1
        if stack[-1].isnumeric():
            return ""
        else:
            return "".join(stack)