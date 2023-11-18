# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        def count(node,d):
            if not node:
                return 
            if d == k:
                ans.append(node.val)
            count(node.left,d+1)
            count(node.right,d+1)
        l = 0
        def tr(node):
            if not node:
                return 
            if node == target:
                count(node,l)
                return 1
            x = tr(node.left)
            y = tr(node.right)
            if x != None:
                node.left = None
                count(node,x)
                return x+1
            elif y!= None:
                node.right = None
                count(node,y)
                return y+1                
        tr(root)
        return ans
    