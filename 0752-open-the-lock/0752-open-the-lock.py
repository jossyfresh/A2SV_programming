class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set(deadends)
        start = "0000"
        queue.append(start)
        len_ = 0
        def Newdigits(string):
            digits = []
            for i in range(4):
                val = string[i]
                digits.append(string[:i] + str((int(val) + 1) % 10) + string[i+1:])
                digits.append(string[:i] + str((int(val) - 1) % 10) + string[i+1:])
            return digits
        if queue[0] in visited:
            return -1
        print(queue)
        while queue:
            n = len(queue)
            for i in range(n):
                code = queue.popleft()
                visited.add(code)
                if code == target:
                    return len_
                newdigits = Newdigits(code)
                for x in newdigits:
                    if x not in visited:
                        queue.append(x)
                        visited.add(x)
            len_ += 1
        print(queue)
        return -1