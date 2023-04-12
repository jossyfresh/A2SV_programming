class Solution:
    def findCircleNum(self, con: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(len(con))}
        for i in range(len(con)):
            for j in range(len(con)):
                if con[i][j] and i!= j:
                    adjlist[i].append(j)
                    adjlist[j].append(i)
        visited = set()
        len_comp = 0
        def dfs(curr_node):
            for val in adjlist[curr_node]:
                if val not in visited:
                    visited.add(val)
                    dfs(val)
        for i in range(len(con)):
            if i not in visited:
                len_comp += 1
                dfs(i)
        return len_comp