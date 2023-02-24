n = int(input())
nums = list(map(int,input().split()))
nums.sort()
flag  = 1
if nums[-3] + nums[-2] > nums[-1]:
    nums[-2],nums[-1] = nums[-1],nums[-2]
    flag = 0
    print("YES")
    print(*nums)
if flag ==1:
    print("NO")
