from typing import List
from collections import defaultdict,Counter,deque

from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        adjlist = defaultdict(list)
        indegree = defaultdict(set)
        for x,y in edges:
            adjlist[x].append(y)
            indegree[y].add(x)
        queue = deque()
       
        for x in range(1,n+1):
            if len(indegree[x]) == 0:
                queue.append(x)
        val = 1
        ans = [1] * n
        visited = set()
        while queue:
            n = len(queue)
            while n:
                n -= 1
                cur = queue.popleft()
                visited.add(cur)
                ans[cur-1] = str(val)
                for node in adjlist[cur]:
                    if node not in visited:
                        indegree[node].remove(cur)
                        if len(indegree[node]) == 0:
                            queue.append(node)
                            visited.add(node)
            val += 1
        return " ".join(ans)