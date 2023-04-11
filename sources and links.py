n = int(input())
sinks = []
source = []
matrix = []
for _ in range(n):
    grid = list(map(int,input().split()))
    matrix.append(grid)
for i in range(n):
    flag = 0
    for j in range(n):
        if matrix[i][j] == 1:
            flag = 1
            break
    if not flag:
        sinks.append(i+1)
for i in range(n):
    flag = 0
    for j in range(n):
        if matrix[j][i] == 1:
            flag = 1
            break
    if not flag:
        source.append(i+1)
source.sort()
sinks.sort()
source.insert(0,len(source))
sinks.insert(0,len(sinks))
print(*source)
print(*sinks)