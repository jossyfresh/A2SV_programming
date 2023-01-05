n = int(input())
dict = {}
nums = list(map(int,input().split()))
for x in nums:
    dict[x]=dict.get(x,0)+1
for key in dict:
    if dict[key]!= n:
         print(key)
         break
