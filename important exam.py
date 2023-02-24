from collections import Counter
n = list(map(int,input().split()))
ans = []
count = 0
for j in range(n[0]):
    ans.append(input())
value = list(map(int,input().split()))
new = list(zip(*ans))
for i in range(n[1]):
    x = list(new[i])
    diction = Counter(x)
    val = diction.most_common()
    val[0] = list(val[0])
    count += val[0][1] * value[i]
print(count)
