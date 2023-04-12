"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, emp: List['Employee'], id: int) -> int:
        ans = [0]
        def dfs(cur_node):
            ans[0] += cur_node.importance
            for x in cur_node.subordinates:
                for y in emp:
                    if x == y.id:
                        dfs(y)
        for x in emp:
            if x.id == id:
                dfs(x)
        return ans[0]