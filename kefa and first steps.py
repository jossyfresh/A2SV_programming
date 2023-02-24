n = int(input())
num = list(map(int,input().split()))
l = 0
r = 1
res = 0
while r <= n-1:
    if num[r] >= num[r-1]:
        r+=1
    else:
        res = max(res,r-l)
        l = r
        r += 1
res = max(res,r-l)
print(res)