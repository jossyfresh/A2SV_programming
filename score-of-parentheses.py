class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for x in s:
            if x == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                    if len(stack) > 1 and stack[-2]!="(":
                        stack[-2] = stack[-1]+stack[-2]
                        stack.pop()
                else:
                    val = stack.pop()
                    stack.pop()
                    stack.append(val*2)
                    if len(stack) > 1 and stack[-2]!="(":
                        stack[-2] = stack[-1]+stack[-2]
                        stack.pop()
            else:
                stack.append(x)
            print(stack)
        return sum(stack)