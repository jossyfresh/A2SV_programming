class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjlist = defaultdict(list)
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        ans = [0] * n
        def dfs(node,parent):
            counts = collections.Counter()
            for child in adjlist[node]:
                if child != parent:
                    counts += dfs(child,node)
            counts[labels[node]] += 1
            ans[node] = counts[labels[node]]
            return counts
        dfs(0,-1)
        return ans