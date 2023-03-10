# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def tr(node1,node2):
            if not node1 and not node2:
                return None
            n = node1.val if node1 else 0
            m = node2.val if node2 else 0
            ans = TreeNode(n+m)
            y = node1.left if node1 else None
            x = node1.right if node1 else None
            l = node2.left if node2 else None
            r = node2.right if node2 else None
            ans.left = tr(y,l)
            ans.right = tr(x,r)
            return ans
        return tr(root1,root2)