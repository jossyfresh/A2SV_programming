n = list(map(int,input().split()))
a = n[0] + n[2]
b = n[1] + n[2]
if a == b:
    print(a+b)
elif a < b:
    print((a*2)+1)
elif b < a:
    print((b*2)+1)