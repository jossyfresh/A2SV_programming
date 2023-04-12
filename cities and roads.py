n = int(input())
matrix = []
for i in range(n):
    grid  = list(map(int,input().split()))
    matrix.append(grid)
edges = set()
for i in range(n):
    for j in range(n):
        if i!=j:
            if matrix[i][j] == 1:
                if (j,i) not in edges:
                    edges.add((i,j))
print(len(edges))