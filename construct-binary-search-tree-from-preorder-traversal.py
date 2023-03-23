# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(root,val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = insert(root.right,val)
            else:
                root.left = insert(root.left,val)
            return root
        dum = TreeNode(0)
        root = None
        dum.left = root
        for x in preorder:
            node = TreeNode(x)
            if root == None:
                root = node
                dum.right = root
            else:
                insert(root,x)
        return dum.right