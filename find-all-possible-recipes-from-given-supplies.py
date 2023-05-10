class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        visited = set()
        supplies = set(supplies)
        adjlist = defaultdict(list)
        degree = Counter()
        ans = []
        for i in range(len(recipes)):
            for j in ingredients[i]:
                if j not in supplies:
                    adjlist[j].append(recipes[i])
                    degree[recipes[i]] += 1
        print(adjlist)
        queue = deque()
        for x in recipes:
            if degree[x] == 0:
                queue.append(x)
        while queue:
            u = queue.popleft()
            ans.append(u)
            for node in adjlist[u]:
                degree[node] -= 1
                if degree[node] == 0:
                    queue.append(node)
        return ans