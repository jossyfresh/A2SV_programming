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
            dfs(node.left)
            dfs(node.right)
            return 
        ans = [0]
        def check(node,target):
            if not node.left and not node.right:
                if target-node.val == 0:
                    ans[0] += 1
                return
            if target-node.val == 0:
                ans[0] += 1
            if node.left:
                check(node.left,target-node.val)
            if node.right:
                check(node.right,target-node.val)
            return 
        dfs(root)
        return ans[0]