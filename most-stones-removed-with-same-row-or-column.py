class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {i:i for i in range(len(stones))}
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        def union(x,y):
            repx = find(x)
            repy = find(y)
            if repx == repy:
                return 
            rep[repy] = repx
        for i in range(len(stones)):
            for j in range(len(stones)):
                x = stones[i]
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    union(i,j)
        visited = set()
        for i in range(len(stones)):
            visited.add(find(i))
        return len(stones) - len(visited)