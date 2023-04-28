class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        self.parents = {}
        self.locked = [[False,0] for i in range(len(parent))]
        for i in range(len(parent)):
            self.graph[parent[i]].append(i)
            self.parents[i] = parent[i]
    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num][0]:
            self.locked[num][0] = True
            self.locked[num][1] = user
            return True
        return False
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num][0]:
            if self.locked[num][1] == user:
                self.locked[num] = [False,0]
                return True
        return False
    def upgrade(self, num: int, user: int) -> bool:
        flagi = 1
        val = num
        while True:
                if self.locked[val][0]:
                    flagi = 0
                    break
                val = self.parents[val] 
                if val == -1:
                    break
        visited = set()
        flag = 0
        def dfs(cur_node):
            nonlocal flag
            visited.add(cur_node)
            if self.locked[cur_node][0]:
                flag = 1
            for node in self.graph[cur_node]:
                if node not in visited:
                    dfs(node)
        check = set()
        dfs(num)
        def unlockall(cur_node):
            check.add(cur_node)
            self.locked[cur_node] = [False,0]
            for node in self.graph[cur_node]:
                if node not in check:
                    unlockall(node)

        if flag and flagi:
            unlockall(num)
            self.locked[num] = [True,user]
            return True
        return False
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)