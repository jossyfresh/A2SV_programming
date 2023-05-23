#User function Template for python3
from collections import deque,defaultdict,Counter

class Solution:
    def findOrder(self,name, N, K):
    # code here
        adjlist = defaultdict(list)
        incoming = Counter()
        letters = set()
        for i in range(len(name)):
            for x in name[i]:
                letters.add(x)
        for i in range(len(name)-1):
            first = name[i]
            second = name[i+1]
            for j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    adjlist[first[j]].append(second[j])
                    incoming[second[j]] += 1
                    break
        ans = []
        visited = set()
        queue= deque()
        for i in letters:
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            n = len(queue)
            while n:
                n -= 1
                cur = queue.popleft()
                ans.append(cur)
                visited.add(cur)
                for node in adjlist[cur]:
                    if node not in visited:
                        incoming[node] -= 1
                        if incoming[node] == 0:
                            queue.append(node)
                            visited.add(node)
 
        return "".join(ans)
    