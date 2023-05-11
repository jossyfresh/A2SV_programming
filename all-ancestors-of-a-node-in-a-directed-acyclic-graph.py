class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjlist = defaultdict(list)
        degree = Counter()
        for x,y in edges:
            adjlist[x].append(y)
            degree[y] += 1
        ans = [set() for i in range(n)]
        queue = deque()
        for x in range(n):
            if degree[x] == 0:
                queue.append(x)
        while queue:
            cur = queue.popleft()
            for node in adjlist[cur]:
                ans[node].add(cur)
                ans[node].update(ans[cur])
                degree[node] -= 1
                if degree[node] == 0:
                    queue.append(node)
        return [sorted(i) for i in ans]