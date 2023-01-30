n = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l = 0
r = 0
ans = []
while r < n[1]:
    if l >= n[0]:
        ans.append(l)
        r+=1
    elif arr2[r] > arr1[l]:
        l+=1
    else:
        ans.append(l)
        r+=1
print(*ans)
