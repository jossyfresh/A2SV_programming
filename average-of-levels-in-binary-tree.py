# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        res = []
        if root:
            queue = deque()
            queue.append(root)
            while queue:
                n = len(queue)
                cur = []
                while n > 0:
                    node = queue.popleft()
                    cur.append(node.val)
                    n -= 1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(cur)
        for x in ans:
            res.append(sum(x)/len(x))
        return res