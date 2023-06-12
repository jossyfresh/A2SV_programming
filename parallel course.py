from collections import defaultdict
from collections import deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    adjlist = defaultdict(list)
    indegree = defaultdict(set)
    for x,y in prerequisites:
        adjlist[x].append(y)
        adjlist[y].append(x)
        indegree[y].add(x)
    queue = deque()
    for i in range(1,n+1):
        if len(indegree[i]) == 0:
            queue.append(i)
    visited = set()
    c = 0
    while queue:
        k = len(queue)
        while k:
            k -= 1
            cur = queue.popleft()
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    indegree[node].remove(cur)
                    if len(indegree[node]) == 0:
                        queue.append(node)
                        visited.add(node)
        c += 1
    if len(visited) == n:
        return c
    return -1
    


        
