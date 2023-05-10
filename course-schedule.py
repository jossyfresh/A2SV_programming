class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = defaultdict()
        adjlist = defaultdict(list)
        for x,y in  prerequisites:
            adjlist[x].append(y)
            incoming[y] = incoming.get(y,0) + 1
        ans = []
        visited = set()
        flag = 0
        queue = deque()
        for x in range(numCourses):
            if x not in incoming:
                queue.append(x)
        while queue:
            n = len(queue)
            while n:
                n -= 1
                x = queue.popleft()
                ans.append(x)
                visited.add(x)
                for node in adjlist[x]:
                    if node in visited:
                        flag = 1
                    if node in incoming:
                        incoming[node] = incoming.get(node,0)-1
                        if incoming[node] == 0:
                            queue.append(node)
                            visited.add(node)
        ans.reverse()
        for x in incoming:
            if incoming[x] > 0:
                flag = 1
        if flag:
            return False
        return True