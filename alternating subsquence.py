t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    maps = []
    i = 1
    maps.append(num[0])
    while i < len(num):
        if maps[-1] < 0:
            if num[i] > 0:
                maps.append(num[i])
            else:
                if num[i] > maps[-1]:
                    maps[-1] = num[i]
        else:
            if num[i] < 0:
                maps.append(num[i])
            else:
                if num[i] > maps[-1]:
                    maps[-1] = num[i]
        i+=1
    print(sum(maps))
