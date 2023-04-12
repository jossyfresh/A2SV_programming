n = int(input())
matrix = []
for i in range(n):
    grid  = list(map(int,input().split()))
    matrix.append(grid)
adjlist = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            if matrix[i][j] == 1:
                adjlist[i].append(j+1)
for i in range(n):
    adjlist[i].insert(0,len(adjlist[i]))
    print(*adjlist[i])