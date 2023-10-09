# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        ans2 = []
        def tr(node,p,ans):
            if not node:
                return False
            if node.val == p.val:
                ans.append(node.val)
                return True
            if tr(node.left,p,ans):
                ans.append(node.val)
                return True
            if tr(node.right,p,ans):
                ans.append(node.val)
                return True
        tr(root,p,ans)
        tr(root,q,ans2)
        ans = ans[::-1]
        ans2 = ans2[::-1]
        if len(ans) > len(ans2):
            for i in range(len(ans)-len(ans2)):
                ans2.append(-((10**9)+1))
        else:
            for i in range(len(ans2)-len(ans)):
                ans.append(-((10**9)+1))
        val = 0
        print(ans)
        print(ans2)
        for i in range(len(ans)-1,-1,-1):
            if ans[i] == ans2[i]:
                val = ans[i]
                break
        return TreeNode(val,None,None)