# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def add(node):
            val = 0
            node1 = node.left
            node2 = node.right
            if node1:
                if node1.left:
                    val += node1.left.val
                if node1.right:
                    val+= node1.right.val
            if node2:
                if node2.left:
                    val += node2.left.val
                if node2.right:
                    val+= node2.right.val
            return val
        ans = 0
        def tr(node):
            nonlocal ans
            if not node:
                return False
            if node.val%2==0:
                ans += add(node)
            tr(node.left)
            tr(node.right)
        tr(root)
        return ans