# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        def dfs(node,level,n):
            if not node:
                return 
            ans[level].append(n)
            left = dfs(node.left,level+1,n*2)
            right = dfs(node.right,level+1,(n*2)+1)
            return 
        dfs(root,1,0) 
        res = 0
        for level in ans:
            x = ans[level]
            res = max(res,(max(x)-min(x))+1)
        return res