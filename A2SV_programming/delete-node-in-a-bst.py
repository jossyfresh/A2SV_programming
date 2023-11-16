# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteNode(root, k):
            if root is None:
                return root
            if root.val > k:
                root.left = deleteNode(root.left, k)
                return root
            elif root.val < k:
                root.right = deleteNode(root.right, k)
                return root
            else:

                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                cur = root.right
                while cur.left:
                    cur = cur.left 
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)
            return root        
        return deleteNode(root,key)
                    
            
            