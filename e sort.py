t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    r = 0
    temp = 0
    count = 0
    while r < (n[0])-1:
        if 2*(nums[r+1]) > nums[r]:
            temp +=1
        else:
            temp = 0
        
        if temp == n[1]:
            temp-=1
            count+=1
        r+=1
    print(count)
        