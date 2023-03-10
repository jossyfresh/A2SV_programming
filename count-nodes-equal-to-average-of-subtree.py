# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def cal(node,arr):
            if not node:
                return 0
            if node:
                arr[1] += 1
            arr[0] += node.val
            cal(node.left,arr)
            cal(node.right,arr)
            return arr
        res = 0
        def tr(node):
            nonlocal res
            if not node:
                return 0
            ans = cal(node,[0,0])
            if ans[0]//ans[1] == node.val:
                res += 1
            tr(node.left)
            tr(node.right)
            return res
        tr(root)
        return res