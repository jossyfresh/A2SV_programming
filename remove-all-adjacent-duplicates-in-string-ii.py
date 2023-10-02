class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([x,1])
        res = ""
        for x,time in stack:
            res += x*time
        return res