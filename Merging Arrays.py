n,m = map(int,input().split())
n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))
l = 0
r = 0
ans = []
while r < m and l < n:
    if n1[l] < n2[r]:
        ans.append(n1[l])
        l+=1
    else:
        ans.append(n2[r])
        r+=1
while l < n:
    ans.append(n1[l])
    l+=1
while r < m:
    ans.append(n2[r])
    r+=1
print(*ans)
