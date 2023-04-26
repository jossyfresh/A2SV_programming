# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], val: int) -> int:
        def dfs(node):
            if not node:
                return
            check(node,val)
            left = dfs(node.left)
            right = dfs(node.right)
        ans = 0
        def check(node,target):
            nonlocal ans
            if not node:
                return 
            if target == node.val:
                ans += 1
            left = check(node.left,target-node.val)
            right = check(node.right,target-node.val)
        dfs(root)
        return ans