# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node,sub):
            if node == None and sub == None:
                return True
            if node == None or sub == None:
                return False
            return check(node.left,sub.left) and check(node.right,sub.right) and node.val == sub.val
        return check(p,q)