n = list(map(int,input().split()))
mat = []
for i in range(n[0]):
    word = input()
    mat.append(word)
def checkword(x, i, j, mat):
    row = 0
    for r in range(len(mat)):
        if mat[r][j] == x:
            row += 1
        if row > 1:
            return False
    col = 0
    for c in range(len(mat[0])):
        if mat[i][c] == x:
            col += 1
        if col > 1:
            return False
    return True
ans = ""
for i in range(n[0]):
    for j in range(n[1]):
        x = mat[i][j]
        if checkword(x,i,j,mat):
            ans+=x
print(ans)
