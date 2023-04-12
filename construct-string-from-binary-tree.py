# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        nodes = []
        def tr(node):
            if not node:
                return True
            nodes.append("(" + str(node.val))
            if tr(node.left) and node.right:
                nodes.append("()")
            tr(node.right)
            nodes.append(")")
        tr(root)
        ans = "".join(nodes)
        ans = list(ans[1:-1])
        new = []
        return "".join(ans)