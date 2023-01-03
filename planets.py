n = int(input())
for i in range(n):
    x = list(map(int,input().split()))
    planets = list(map(int,input().split()))
    p = set(planets)
    count = 0
    if x[1] == 1:
        count = len(p)
    else:
        for j in p:
            if planets.count(j) >= x[1]:
                count+=x[1]
            else:
                count+=planets.count(j)
    print(count)
