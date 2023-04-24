from collections import defaultdict
n = int(input())
while n != 0:
    adjlist = defaultdict(list)
    l = int(input())
    for _ in range(l):
        x,y = map(int,input().split())
        adjlist[x].append(y)
        adjlist[y].append(x)
    color = [0 for i in range(n)]
    flag = [0]
    visited = set()
    def dfs(cur_node):
        visited.add(cur_node)
        for x in adjlist[cur_node]:
            if color[cur_node-1] == color[x-1]:
                flag[0] = 1
            if not color[x-1]:
                if color[cur_node-1] == 1:
                    color[x-1] = -1
                else:
                    color[x-1] = 1  
            if x not in visited:
                dfs(x)  
    for i in range(1,n+1):
        if not color[i-1]:
            color[i-1] = 1
        visited.add(i)
        dfs(i)
    if flag[0] == 1:
        print("NOT BICOLOURABLE.")
    else:
        print("BICOLOURABLE.")
    n = int(input())
else:
    exit()
