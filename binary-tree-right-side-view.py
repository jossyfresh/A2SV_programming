# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        heig = set()
        def tr(node,height):
            if not node:
                return height
            if height not in heig:
                ans.append(node.val)
                heig.add(height)
            tr(node.right,height+1)
            tr(node.left,height+1)
        tr(root,0)
        return ans