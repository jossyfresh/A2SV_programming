# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        res = []
        def path(node):
            if not node:
                return False
            if not node.left and not node.right:
                ans.append(int("".join(res + [str(node.val)])))
                return False
            res.append(str(node.val))
            path(node.left)
            path(node.right)
            res.pop()
        path(root)
        return sum(ans)