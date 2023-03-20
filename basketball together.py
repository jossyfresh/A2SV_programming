n,d = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
nums.reverse()
new = [] 
count = 0
for i in range(len(nums)):
    if len(new) == len(nums):
        break
    x = nums[i]
    Sum = 0
    while Sum <= d:
        if len(new) == len(nums):
            break
        new.append(x)
        Sum+=x
    if Sum > d:
        count+=1
print(count)