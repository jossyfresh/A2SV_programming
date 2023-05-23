class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = {i:i for i in range(n)}
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
            if rank[repx] == rank[repy]:
                rank[repx] += 1
        ans = [True] * len(requests)
        for i in range(len(requests)):
            a,b = requests[i]
            a = find(a)
            b = find(b)
            for x,y in restrictions:
                x = find(x)
                y = find(y)
                if (a == x and b== y) or (a == y and b == x):
                    ans[i] = False
            if ans[i]:
                union(a,b)
        return ans