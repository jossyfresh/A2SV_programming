# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        nodes = []
        def tr(node):
            if not node:
                return False
            if not node.left and not node.right:
                ans.append( "->".join(nodes+[str(node.val)]))
                return False
            nodes.append(str(node.val))
            tr(node.left)
            tr(node.right)
            nodes.pop()
        tr(root)
        return ans