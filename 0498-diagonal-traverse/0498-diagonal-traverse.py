class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        ans = []
        k = 0
        up = True
        i = 0
        j = 0
        if col == 1:
            while k < row*col:
                ans.append(mat[i][j])
                i+=1
                k+=1
        elif row == 1:
            while k < col*row:
                ans.append(mat[i][j])
                j+=1
                k+=1
        else:
            while k < row * col:
                if up and i==0 and j==0:
                    ans.append(mat[i][j])
                    up = False
                    j+=1
                elif not up and j >= 0 and i <= row-1:
                    if j == 0 and i!= row-1:
                        up = True
                        ans.append(mat[i][j])
                        i+= 1
                    elif i == row-1 and j!= 0:
                        up = True
                        ans.append(mat[i][j])
                        j+=1
                    elif i == row-1 and j==0:
                        up = True
                        ans.append(mat[i][j])
                        j+=1
                    else:
                        ans.append(mat[i][j])
                        i += 1
                        j -= 1
                elif up and i >= 0 and j <= col-1:
                    if i == 0 and j!= col-1:
                        up = False
                        ans.append(mat[i][j])
                        j += 1
                    elif j == col-1 and i!=0:
                        up = False
                        ans.append(mat[i][j])
                        i+=1
                    elif j == col-1 and i==0:
                        up = False
                        ans.append(mat[i][j])
                        i+=1
                    else:
                        ans.append(mat[i][j])
                        i -= 1
                        j += 1
                k+=1
        return ans