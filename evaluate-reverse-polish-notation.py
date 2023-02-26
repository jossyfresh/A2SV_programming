class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "+-*/"
        for x in tokens:
            if x in op:
                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    stack.append(a+b)
                elif x == "*":
                    stack.append(a*b)
                elif x == "/":
                    stack.append(int(a/b))
                else:
                    stack.append(a-b)
            else:
                stack.append(int(x))
        return int(stack[-1])