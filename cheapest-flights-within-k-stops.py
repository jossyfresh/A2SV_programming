class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjlist = defaultdict(list)
        for source,destination,cost in flights:
            adjlist[source].append((cost,destination,0))
        def dijkstra(graph,source,destination,k):
            distances = {i:float("inf") for i in range(n)}
            distances[source] = 0
            queue = [(-1,0,source)]
            visited = set()
            while queue:
                stops,cur_dist,cur_node = heapq.heappop(queue)
                if stops == k:
                    continue
                for cost,dest,stop in graph[cur_node]:
                    if stops < k:
                        newDist = cost + cur_dist
                        if newDist <= distances[dest]:
                            distances[dest] = newDist
                            heapq.heappush(queue,(stops + 1,newDist,dest))
            if distances[destination] != float("inf"):
                return distances[destination]
            return -1
        return dijkstra(adjlist,src,dst,k)