class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rep = {i:i for i in range(n)}
        rank = [0] * n
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x:x[2])
        edges.sort(key=lambda x:x[2])
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
        ans = [False] * len(queries)
        x = 0
        for i in range(len(queries)):
            a,b,val,ind = queries[i]
            if find(a) == find(b):
                ans[ind] = True
            while x < len(edges) and edges[x][2] < val:
                union(edges[x][0],edges[x][1])
                if find(a) == find(b):
                    ans[ind] = True
                x += 1
        return ans