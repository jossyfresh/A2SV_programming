class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        strlength = len(strs[0])
        rep = [i for i in range(len(strs))]
        rank = [0] * n
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
            rank[repx] += 1
        for i in range(len(strs)):
            for j in range(len(strs)):
                c = 0
                if find(i) == find(j):
                    continue
                for k in range(strlength):
                    if strs[i][k] != strs[j][k]:
                        c += 1
                if c <= 2:
                    union(i,j)
        count = Counter(rep)
        return len(count)