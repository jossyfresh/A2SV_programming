# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        def tr(y,x,node):
            if not node:
                return 
            ans[y].append(x)
            tr(y+1,x*2,node.left)
            tr(y+1,x*2+1,node.right)
        tr(0,0,root)
        print(ans)
        max_ = 0
        for x in ans:
            lisst = ans[x]
            max_ = max(max_,(max(lisst) - min(lisst))+1)
        return max_