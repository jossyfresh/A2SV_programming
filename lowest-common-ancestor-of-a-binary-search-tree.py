# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr = []
        arr2 = []
        def hasPath(root, arr, x):
            if (not root):
                return False
            arr.append(root.val)    
            if (root.val== x):    
                return True
            if (hasPath(root.left, arr, x) or
                hasPath(root.right, arr, x)):
                return True
            arr.pop(-1)
            return False
        hasPath(root,arr,p.val)
        hasPath(root,arr2,q.val)
        if len(arr) > len(arr2):
            for i in range(len(arr)-len(arr2)):
                arr2.append(-((10**9)+1))
        else:
            for i in range(len(arr2)-len(arr)):
                arr.append(-((10**9)+1))
        print(arr)
        print(arr2)
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == arr2[i]:
                data = arr[i]
                break
        while root != None:
            if root.val == data:
                return root
            if root.val > data:
                root = root.left
            else:
                root = root.right