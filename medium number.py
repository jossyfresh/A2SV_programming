t = int(input())
for i in range(t):
    x = list(map(int,input().split())) 
    for j in range(len(x)):
        if x[j]!= min(x) and x[j]!=max(x):
            print(x[j])