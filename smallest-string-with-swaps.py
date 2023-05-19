class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {i:i for i in range(len(s))}
        rank = [0] * len(s)
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        ms = defaultdict(list)
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
        for x,y in pairs:
            union(x,y)
        for i in range(len(s)):
            val = find(i)
            ms[val].append(s[i])
        for m in ms:
            ms[m].sort()
            ms[m].reverse()
        ans = ""
        for i in range(len(s)):
            x = find(i)
            ans += ms[x].pop()
        return ans