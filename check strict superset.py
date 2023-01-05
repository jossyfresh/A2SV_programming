a = set(map(int,input().split()))
n = int(input())
check = True
for i in range(n):
    x = set(map(int,input().split()))
    if len(x) > len(a):
        check = False
    else:
        for k in x:
            if k not in a:
                check = False
print(check)
