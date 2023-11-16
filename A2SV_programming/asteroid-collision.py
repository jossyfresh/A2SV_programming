class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while True:
                if not stack:
                    stack.append(x)
                    break
                else:
                    if stack[-1] * x > 0:
                        stack.append(x)
                        break
                    else:
                        if stack[-1] > 0 and x < 0:
                            if abs(stack[-1]) == abs(x):
                                stack.pop()
                                break
                            elif abs(stack[-1]) < abs(x):
                                stack.pop()
                            else:
                                break
                        else:
                            stack.append(x)
                            break
        return stack


