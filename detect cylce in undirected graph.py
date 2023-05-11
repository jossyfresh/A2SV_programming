from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		flag = [0]
        def dfs(cur_node,parent):
            visited.add(cur_node)
            for node in adj[cur_node]:
                if node not in visited:
                    if dfs(node,cur_node):
                        return True
                else:
                    if node != parent:
                     return True
            return False
                
        for x in range(v):
            if x not in visited:
                if dfs(x,None):
                    return True
        return False
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends