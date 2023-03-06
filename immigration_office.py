from bisect import bisect_right
 
 
t = int(input())
x = list(map(str,input().split()))
n = int(input())
for i in range(n):
    val = bisect_right(x,input())
    print(val)
