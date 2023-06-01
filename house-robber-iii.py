# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node,c):
            if (node,c) in memo:
                return memo[(node,c)]
            if not node:
                return 0
            x = 0
            y = 0
            z = 0
            w = 0
            a = 0
            if c:
                x = dfs(node.left,False)
                y = dfs(node.right,False) 
                a = x+y+node.val
            z = dfs(node.left,True)
            w = dfs(node.right,True)
            val =  max(a,w+z)
            memo[(node,c)] = val
            return val
        return dfs(root,True)