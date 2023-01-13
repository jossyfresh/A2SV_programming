class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [[] for i in range(r)]
        k = 0
        l = 0
        if r*c != len(mat)*len(mat[0]):
           return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[l].append(mat[i][j])
                k+=1
                if k == c:
                    k = 0
                    l += 1
        return ans
