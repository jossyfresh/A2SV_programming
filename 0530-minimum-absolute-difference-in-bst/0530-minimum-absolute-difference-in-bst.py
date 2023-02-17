# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        data = []
        min_ = inf
        def inorder(node):
            if node:
                inorder(node.left)
                data.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in range(len(data)-1):
            val = abs(data[i]-data[i+1])
            min_ = min(val,min_)
        return min_
        