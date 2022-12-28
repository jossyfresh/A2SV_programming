class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        for i in range(len(matches)):
            if matches[i][0] in dict1:
                dict1[matches[i][0]]+=1
            else:
                dict1[matches[i][0]]=1
            if matches[i][1] in dict2:
                dict2[matches[i][1]]+=1
            else:
                dict2[matches[i][1]]=1
        win = []
        lose = []
        for x in dict1:
            if x not in dict2:
                win.append(x)
        for y in dict2:
            if dict2[y] == 1:
                lose.append(y)
        win.sort()
        lose.sort()
        answer = []
        answer.append(win)
        answer.append(lose)
        return answer