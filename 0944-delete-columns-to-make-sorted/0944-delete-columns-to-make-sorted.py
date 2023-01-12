class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = list(zip(*strs))
        count = 0
        for i in range(len(col)):
            for j in range(len(col[i])-1):
                if ord(col[i][j]) > ord(col[i][j+1]):
                    count += 1
                    break
        return count