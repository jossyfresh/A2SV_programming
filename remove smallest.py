t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    flag = 0
    nums.sort()
    for j in range(n-1):
        if abs(nums[j] - nums[j+1]) > 1:
            print("NO")
            flag = 1
            break
    if flag == 0:
        print("YES")
