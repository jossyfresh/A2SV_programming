class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjlist = defaultdict(list)
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        ans = [0]
        visited = set()
        def dfs(cur,par):
            visited.add(cur)
            if len(adjlist[cur]) == 1 and adjlist[cur][0] == par:
                if values[cur] % k == 0:
                    ans[0] += 1
                    return 0
                return values[cur]
            total = values[cur]
            for node in adjlist[cur]:
                if node not in visited:
                    total += dfs(node,cur)
            if total % k == 0:
                ans[0] += 1
                return 0
            return total 
        dfs(0,-1)
        return ans[0]