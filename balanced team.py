n = int(input())
num = list(map(int,input().split()))
l = 0
r = 1
k = 0
num.sort()
res= 0
while r < n:
    k = num[r]-num[l]
    if k > 5:
        res = max(res,r-l)
        l+=1
    else:
        r+=1
res = max(res,r-l)
print(res)
