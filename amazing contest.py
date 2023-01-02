n = int(input())
x = list(map(int,input().split()))
maxi = x[0]
mini = x[0]
count = 0
for i in range(1,n):
  if x[i] > maxi:
    count+=1
    maxi =max(maxi,x[i])
  elif x[i] < mini:
    count+=1
    mini =min(mini,x[i])
  else:
    continue
print(count)
