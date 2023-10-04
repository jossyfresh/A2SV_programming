class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = defaultdict(list)
        for x,y,z in times:
            adjlist[x].append([y,z])
        def dijkstra(graph, start):
            distances = {i: float('inf') for i in range(1,n+1)}
            distances[start] = 0
            visited = set()
            priority_queue = [(0, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances
        distances = dijkstra(adjlist,k)
        ans = 0
        for x in distances:
            if distances[x] == float('inf'):
                return -1
            ans = max(ans,distances[x])
        return ans