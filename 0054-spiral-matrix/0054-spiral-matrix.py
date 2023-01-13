class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row = m-1
        col = n-1
        colend,rowend,l,i,j = 0,1,0,0,0
        ans = []
        down = True
        right = True
        while l < m*n:
            ans.append(matrix[i][j])
            if j <= col and right and down:
                if j == col:
                    right = False
                    col-=1
                    i+=1
                else:
                    j+=1
            elif i<=row and not right and down:
                if i == row:
                    row-=1
                    down = False
                    j-=1
                else:
                    i+=1
            elif j>=colend and not right and not down:
                if j == colend:
                    colend+=1
                    right = True
                    i-=1
                else:
                    j-=1
            elif i >= rowend and not down and right:
                if i == rowend:
                    rowend+=1
                    down = True
                    j+=1
                else:
                    i-=1
            l+=1
        return ans