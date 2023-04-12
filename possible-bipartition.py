class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(n)}
        for x,y in dislikes:
            adjlist[x-1].append(y-1)
            adjlist[y-1].append(x-1)
        color = [0 for i in range(n)]
        flag = [0]
        visited = set()
        def dfs(cur_node):
            visited.add(cur_node)
            for x in adjlist[cur_node]:
                if color[cur_node] == color[x]:
                    flag[0] = 1
                if not color[x]:
                    if color[cur_node] == 1:
                        color[x] = -1
                    else:
                        color[x] = 1  
                if x not in visited:
                    dfs(x)  
        for i in range(n):
            if not color[i]:
                color[i] = 1
            visited.add(i)
            dfs(i)
        print(color)
        return not flag[0]