# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes = list(map(int,input().split()))
nums = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
happiness = 0
for x in nums:
    if x in a:
        happiness+=1
    elif x in b:
        happiness-=1
print(happiness)
