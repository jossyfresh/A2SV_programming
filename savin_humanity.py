t = int(input())
for k in range(t):
    n,m = map(int,input().split())
    if m > 10**3:
        m = 10**3
    num = input()
    num = list(num)
    new = []
    for x in range(m):
        new = []
        for i in range(n):
            if i < len(num)-1 and num[i+1] == "1" and i > 0 and num[i-1] == "1":
                new.append(num[i])
            elif i < len(num)-1 and num[i+1] == "1":
                new.append("1")
            elif i > 0 and num[i-1] == "1":
                new.append("1")
            else:
                new.append(num[i])
        num = new
    print("".join(num))