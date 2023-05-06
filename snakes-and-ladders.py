class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        row = len(board)-1
        n = len(board)
        mat = copy.deepcopy(board)
        m = {}
        col = 0
        num = 1
        for i in range(len(board)**2):
            mat[row][col] = num
            m[num] = (row,col)
            if (len(board)- row)% 2 !=0:
                if col < len(board)-1:
                    col+=1
                else:
                    row -= 1
                    col = len(board)-1
            else:
                if col > 0:
                    col -= 1
                else:
                    row -= 1
                    col = 0
            num += 1
        queue = deque()
        queue.append(1)
        visited = set()
        len_ = 0
        while queue:
            n = len(queue)
            while n:
                n -= 1
                cur = queue.popleft()
                if cur == len(board)**2:
                    return len_
                for x in range(cur+1,min(cur+6,len(board)**2)+1):
                    i,j = m[x]
                    if board[i][j] == -1:
                        val = x
                    else:
                        val = board[i][j]
                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
                print(queue)
            len_ += 1
        return -1