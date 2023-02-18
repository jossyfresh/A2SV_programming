# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        value = []
        def inorder(node):
            if node:
                inorder(node.left)
                value.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in range(len(value)-1):
            if value[i] >= value[i+1]:
                return False
        return True
                
                