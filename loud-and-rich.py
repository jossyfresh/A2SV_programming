class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adjlist = defaultdict(list)
        degree = Counter()
        for x,y in richer:
            adjlist[x].append(y)
            degree[y] += 1
        ans = [set() for i in range(len(quiet))]
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
        print(ans)
        res = []
        for i in range(len(ans)):
            ans[i] = list(ans[i])
            Max = i
            for j in range(len(ans[i])):
                if quiet[ans[i][j]] < quiet[Max]:
                    Max = ans[i][j]
            res.append(Max)
        return res