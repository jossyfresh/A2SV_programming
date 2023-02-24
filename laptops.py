n = int(input())
nums = []
for i in range(n):
    x = list(map(int,input().split()))
    nums.append(x)
nums.sort(key = lambda x:x[0])
flag = 1
for j in range(len(nums)-1):
    if nums[j][1] > nums[j+1][1]:
        print("Happy Alex")
        flag = 0
        break
if flag == 1:
    print("Poor Alex")