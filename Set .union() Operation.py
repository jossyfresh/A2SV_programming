n=int(input())
eng = input().split()
b = int(input())
frc = input().split()
unique = []
for x in eng :
    if x not in unique:
        unique.append(x)
for y in frc:
    if y not in unique:
        unique.append(y)
print(len(unique))
