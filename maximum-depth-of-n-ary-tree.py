"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_ = [0]
        def dfs(node,height):
            if node:
                height+=1
            if not node.children:
                max_[0] = max(max_[0],height)
            for x in node.children:
                dfs(x,height)
        if root:
            dfs(root,0)
        return max_[0]