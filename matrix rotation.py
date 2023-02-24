t = int(input())
for n in range(t):
    i,j = map(int,input().split())
    x,y = map(int,input().split())
    l = 0
    flag = 0
    while l < 4:
        if i < j and x < y and i < x and j < y:
            print("YES")
            flag = 1
            break
        temp = i
        i = x
        x = y
        y = j
        j = temp
        l+=1
    if flag == 0:
        print("NO")