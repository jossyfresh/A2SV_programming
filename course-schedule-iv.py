class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = defaultdict(list)
        indegree = defaultdict(set)
        for x,y in prerequisites:
            adjlist[x].append(y)
            indegree[y].add(x)
        graph = [[False for i in range(numCourses)] for i in range(numCourses)]
       
        queue = deque()
        for i in range(numCourses):
            queue.append(i)
            visited = set()
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                for node in adjlist[cur]:
                    graph[i][node] = True
                    if node not in visited:
                        queue.append(node)
        ans = []
        print(graph)
        for i,j in queries:
            ans.append(graph[i][j])
        return ans