class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rep = {i:i for i in range(len(points))}
        rank = [0] * len(points)
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        def union(x,y):
            repx = find(x)
            repy = find(y)
            if repx == repy:
                return 
            if rank[repx] < rank[repy]:
                repx,repy = repy,repx
            rep[repy] = repx
            if rank[repx] == rank[repy]:
                rank[repx] += 1
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x = points[i]
                y = points[j]
                val = abs(x[0] - y[0]) + abs(x[1] - y[1])
                edges.append((i,j,val))
        edges.sort(key=lambda x: x[2])
        ans = 0
        for x,y,val in edges:
            if find(x) != find(y):
                ans += val
                union(x,y)
        return ans