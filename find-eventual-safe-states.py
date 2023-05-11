class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        degree = [set(x) for x in graph]
        ans = []
        queue = deque()
        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
            else:
                for x in graph[i]:
                    adjlist[x].append(i)
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for node in adjlist[cur]:
                degree[node].remove(cur)
                if len(degree[node]) == 0: 
                    queue.append(node)
        return sorted(ans)