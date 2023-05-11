class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        degree = set(i for i in range(n))
        indegree = [set() for i in range(n)]
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
            indegree[x].add(y)
            indegree[y].add(x)
        adjlist = defaultdict(list)
        degree = set(i for i in range(n))
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        ans = []
        flag = 0
        queue = deque()
        for i in range(n):
            if len(indegree[i]) == 0:
                ans.append(i)
                flag = 1
            elif len(indegree[i]) == 1:
                queue.append(i)
        if flag:
            return ans
        visited = set()
        while queue:
            n = len(queue)
            if len(degree) == 1 or len(degree) == 2:
                break
            while n:
                n -= 1
                cur = queue.popleft()
                visited.add(cur)
                for node in adjlist[cur]:
                    indegree[node].remove(cur)
                    if len(indegree[node]) == 1:
                        queue.append(node)
                degree.remove(cur)
        return degree