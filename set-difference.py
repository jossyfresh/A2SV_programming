n = int(input())
eng = set(map(int,input().split()))
m = int(input())
frc = set(map(int,input().split()))
x = set()
x = eng.difference(frc)
print(len(x))