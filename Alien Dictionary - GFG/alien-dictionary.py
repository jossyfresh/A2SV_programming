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
    
                
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends