class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road = set()
        for x,y in roads:
            road.add((x,y))
        adjlist = {i:[] for i in range(n)}
        max_ = 0
        for x,y in roads:
            adjlist[x].append(y)
            adjlist[y].append(x)
        adj = [[] for i in range(n)]
        for x in adjlist:
            adj[x] = adjlist[x]
        print(adj)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if (i,j) in road or (j,i) in road:
                        count = len(adj[i]) + len(adj[j]) - 1
                    else:
                        count = len(adj[i]) + len(adj[j]) 
                    max_ = max(max_,count)
        return max_