class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i:i for i in range(1,n+1)}
        size = {i:1 for i in range(1,n+1)}
        adjlist = defaultdict(list)
        for x,y,z in roads:
            adjlist[x].append(y)
            adjlist[y].append(x)
        visited = set()
        queue = deque()
        queue.append(1)
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
        def find(x):
            num = x
            while num != rep[num]:
                num = rep[num]
            return num
        def union(x,y):
            repx = find(x)
            repy = find(y)
            sizex = size[repx]
            sizey = size[repy]
            if sizex >= sizey:
                rep[repy] = repx
                size[repx] = sizex + sizey
            else:
                rep[repx] = repy
                size[repy] = sizey + sizex
        for x,y,z in roads:
            if x < y:
                union(x,y)
            else:
                union(y,x)
        min_ = 10**5

        for x,y,z in roads:
            if find(x) ==  find(y) and x in visited and y in visited:
                min_ = min(min_,z)
        return min_