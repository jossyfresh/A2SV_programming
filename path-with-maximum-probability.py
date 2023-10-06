class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjlist = defaultdict(list)
        for i in range(len(edges)):
            x,y = edges[i]
            adjlist[x].append((y,succProb[i]))
            adjlist[y].append((x,succProb[i]))
        def dijkstra(graph,start,end_node):
            distance = defaultdict(int)
            distance[start] = 1
            queue = [(1,start)]
            visited = set()
            while queue:
                weight,curNode = heapq.heappop(queue)
                weight = abs(weight)
                if curNode in visited:
                    continue
                visited.add(curNode)
                for nei,wei in graph[curNode]:
                    dist = weight * wei
                    if dist > distance[nei]:
                        distance[nei] = dist
                        heapq.heappush(queue, (-dist,nei))
            return distance[end_node]
        return dijkstra(adjlist,start_node,end_node)