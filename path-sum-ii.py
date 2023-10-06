# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def dfs(node,path,target):
            if not node.left and not node.right:
                if target-node.val == 0:
                    ans.append(tuple(path + [node.val]))
                return
            if node.left: 
                dfs(node.left,path + [node.val],target - node.val)
            if node.right:
                dfs(node.right,path + [node.val],target - node.val)
        dfs(root,[],targetSum)
        return ans