class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        m = Counter(s)
        stack = []
        letter = set()
        for x in s:
            while stack and ord(stack[-1]) >= ord(x) and m[stack[-1]] > 1:
                if x in letter:
                    m[x]-=1
                    break
                val = stack.pop()
                m[val]-=1
                letter.remove(val)
            if x not in letter:
                stack.append(x)
                letter.add(x)
        return "".join(stack)