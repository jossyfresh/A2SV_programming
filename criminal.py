t = int(input())
for k in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    r = 0
    l = 0
    count = 0
    while l < len(num)-1:
        if num[l] != 0:
            break
        l+=1
    while l < len(num)-1:
        if num[l] == 0:
            count+=1
        else:
            count+=num[l]
        l+=1
    print(count)
