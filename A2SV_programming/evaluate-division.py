class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjlist = defaultdict(list)
        visited = set()
        for i in range(len(equations)):
            x,y = equations[i]
            adjlist[x].append((y,values[i]))
            adjlist[y].append((x,1/values[i]))
            visited.add(x)
            visited.add(y)
        print(adjlist)
        def dijkstra(graph,start,end_node):
            distance = defaultdict(int)
            if start not in visited or end_node not in visited:
                return 0
            distance[start] = 1
            queue = [(1,start)]
            visit = set()
            while queue:
                weight,curNode = heapq.heappop(queue)
                weight = abs(weight)
                if curNode in visit:
                    continue
                visit.add(curNode)
                for nei,wei in graph[curNode]:
                    dist = weight * wei
                    if dist > distance[nei]:
                        distance[nei] = dist
                        heapq.heappush(queue, (-dist,nei))
            return distance[end_node]
        ans = []
        for x,y in queries:
            val = dijkstra(adjlist,x,y)
            if val > 0:
                ans.append(val)
            else:
                ans.append(-1)
        return ans