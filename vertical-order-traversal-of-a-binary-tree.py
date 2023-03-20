# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        final = []
        def tr(y,x,node):
            if not node:
                return 
            ans.append([y,x,node.val])
            tr(y+1,x-1,node.left)
            tr(y+1,x+1,node.right)
        tr(0,0,root)
        ans.sort(key = lambda x: x[1])
        print(ans)
        def group(arr):
            new = {}
            for x in arr:
                if x[1] in new:
                    y = new[x[1]]
                    y.append([x[0],x[2]])
                    new[x[1]] = y
                else:
                    new[x[1]] = [[x[0],x[2]]]
            return new
        def srt(arr):
            arr.sort(key = lambda x: x[0])
            new = []
            j = arr[0][0]
            i = 0
            temp = []
            while i < len(arr):
                x = arr[i]
                if x[0] == j:
                    temp.append(x[1])
                    i+=1
                else:
                    new.append(sorted(temp))
                    temp = []
                    j = x[0]
            if temp:
                new.append(sorted(temp))
            res = []
            for i in range(len(new)):
                x = new[i]
                for j in range(len(x)):
                    res.append(x[j])
            return res
        print(ans)
        print(group(ans))
        new = group(ans)
        for x in new:
            v = new[x]
            final.append(srt(v))
        return final