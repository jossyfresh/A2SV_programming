class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        rep = {i:i for i in range(len(source))}
        rank = [0] * len(source)
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        ms = defaultdict(dict)
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
        for x,y in allowedSwaps:
            union(x,y)
        for i in range(len(source)):
            val = find(i)
            if source[i] in ms[val]:
                x = ms[val][source[i]]
                ms[val][source[i]] = x+1
            else:
                ms[val][source[i]] = 1
        ans = 0
        print(rep)
        print(ms)
        for i in range(len(target)):
            val = find(i)
            if target[i] not in ms[val]:
                ans += 1
            else:
                x = ms[val][target[i]]
                ms[val][target[i]] = x - 1
                if ms[val][target[i]] == 0:
                    ms[val].pop(target[i])
        return ans