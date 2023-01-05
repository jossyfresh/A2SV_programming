size = list(map(int,input().split()))
dict = {}
for i in range(size[0]):
    x = input()
    dict[i+1] = x
for j in range(size[1]):
    y = input()
    if y in dict.values():
        keys = [k for k, v in dict.items() if v == y]
        for x in keys:
            print(x,end = " ")
        print()
    else:
        print(-1)
        
