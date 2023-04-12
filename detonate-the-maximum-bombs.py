class Solution:
    def maximumDetonation(self, bomb: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(len(bomb))}
        for i in range(len(bomb)):
            for j in range(len(bomb)):
                if i == j:
                    continue
                x1 = bomb[i][0]
                x2 = bomb[j][0]
                y1 = bomb[i][1]
                y2 = bomb[j][1]
                if math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)) <= bomb[i][2]:
                    adjlist[i].append(j)
        print(adjlist)
        def dfs(cur_node):
            visited.add(cur_node)
            for x in adjlist[cur_node]:
                if x not in visited:
                    visited.add(x)
                    dfs(x) 
        max_ = 0       
        for i in range(len(bomb)):
            visited = set()
            dfs(i)
            max_ = max(max_,len(visited))

        return max_