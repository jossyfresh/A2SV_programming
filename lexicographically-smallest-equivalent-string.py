class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {chr(i):chr(i) for i in range(97,97+26)}
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
            if ord(repx) < ord(repy):
                rep[repy] = repx
            else:
                rep[repx] = repy
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = ""
        for i in range(len(baseStr)):
            val = find(baseStr[i])
            ans += val
        return ans