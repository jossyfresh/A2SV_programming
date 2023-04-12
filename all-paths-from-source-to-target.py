class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(path,curr_node):
            if path[-1] == len(graph)-1:
                res.append(path)
                return 
            for i in range(len(graph[curr_node])):
                dfs(path + [graph[curr_node][i]],graph[curr_node][i])
        dfs([0],0)
        return res