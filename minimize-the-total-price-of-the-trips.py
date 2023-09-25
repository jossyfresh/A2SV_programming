class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        frequent = defaultdict(int)
        def dfs(cur,path,end):
            path.add(cur)
            visited.add(cur)
            if cur == end:
                for n in path:
                    frequent[n] += 1
                return True
            for node in adjlist[cur]:
                if node not in visited and dfs(node,path,end):
                    return True
            path.remove(cur)
            return False
        for i,j in trips:
            visited = set()
            dfs(i,set(),j)
        @cache
        def dp(cur,par,half):
            res1 = float("inf")
            if not half:
                res1 = price[cur] // 2 * frequent[cur]
                for node in adjlist[cur]:
                    if node != par:
                        res1 += dp(node,cur,True)
            res2 = price[cur] * frequent[cur]
            for node in adjlist[cur]:
                if node != par:
                    res2 += dp(node,cur,False)
            return min(res1,res2)
        return dp(0,-1,False)