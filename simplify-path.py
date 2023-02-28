class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        print(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "" or s[i] == ".":
                continue
            elif s[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        ans = ""
        for i in stack:
            ans+=("/" + i)
        if ans:return ans
        else: return "/"