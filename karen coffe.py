n,k,m = map(int,input().split())
num = [0]*200002
for p in range(n):
    i,j = map(int,input().split())
    num[i]+= 1
    num[j+1] -= 1
Sum = 0
new = []
for x in num:
    Sum+=x
    new.append(Sum)
for l in range(len(new)):
    if new[l] >= k:
        new[l] = 1
    else:
        new[l] = 0
Sum = 0
for r in range(len(new)):
    Sum+=new[r]
    new[r] = Sum
for a in range(m):
    c,d = map(int,input().split())
    print(new[d]-new[c-1])