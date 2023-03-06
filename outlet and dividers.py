t = int(input())
for k in range(t):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    nums.reverse()
    count = 0
    if n <= 2:
        print("0")
    else:
        Sum = 2
        for x in nums:
            Sum+=x
            count += 1
            Sum-=1
            if Sum >= n:
                break
        if Sum >= n:
            print(count)
        else:
            print(-1)