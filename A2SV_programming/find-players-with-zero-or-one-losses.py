class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        for i in range(len(matches)):
            dict1[matches[i][0]] = dict1.get(matches[i][0],0)+1
            dict2[matches[i][1]] = dict2.get(matches[i][1],0)+1
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