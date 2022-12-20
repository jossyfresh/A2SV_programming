words = []
n = int(input())
for i in range(n):
    words.append(input())
mapofword={} 
for word in words:
    mapofword[word]=mapofword.get(word,0)+1
print(len(mapofword))
for key in mapofword:
    print(mapofword.get(key),end=" ")
