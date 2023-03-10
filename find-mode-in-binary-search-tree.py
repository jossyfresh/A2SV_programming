# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import statistics
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        def tr(node):
            if node:
                tr(node.left)
                nums.append(node.val)
                tr(node.right)
        tr(root)
        ans = []
        y = statistics.mode(nums)
        m = Counter(nums)
        n = m[y]
        for x in nums:
            if m[x] == n:
                if x not in ans:
                    ans.append(x)
        return ans