class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        indegree = Counter()
        for x,y in adjacentPairs:
            adjlist[x].append(y)
            adjlist[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        ans = []
        def dfs(cur_node):
            visited.add(cur_node)
            ans.append(cur_node)
            for node in adjlist[cur_node]:
                if node not in visited:
                    dfs(node)
        for node in indegree:
            if indegree[node] == 1:
                visited = set()
                dfs(node)
                return ans