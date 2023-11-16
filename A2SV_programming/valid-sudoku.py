class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = [[],[],[]]
        for i in range(9):
            if i == 3 or i == 6:
                if len(set(a[0])) == len(a[0]) and len(set(a[1])) == len(a[1]) and len(set(a[2])) == len(a[2]):
                    a = [[],[],[]]
                else:
                    return False
                    a = [[], [], []]
            check = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in check:
                        return False
                    if j <= 2:
                        a[0].append(board[i][j])
                    elif j <= 5 and j > 2:
                        a[1].append(board[i][j])
                    else:
                        a[2].append(board[i][j])
                    check.append(board[i][j])
        if not (len(set(a[0])) == len(a[0]) and len(set(a[1])) == len(a[1]) and len(set(a[2])) == len(a[2])): 
            return False

        for i in range(9):
            ch = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in ch:
                        return False
                    ch.append(board[j][i])
        return True

        