class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        for x in equations:
            rep[x[0]] = x[0]
            rep[x[3]] = x[3]
        def find(x):
            let = x
            while let != rep[let]:
                let = rep[let]
            return let
        flag = 0
        novalid = set()
        def union(x,y):
            nonlocal flag
            repx = find(x)
            repy = find(y)
            if repx != repy:
                rep[repy] = repx
        for letter in equations:
            if letter[1:2] == "=":
                union(letter[0],letter[3])
        for letter in equations:
            if letter[1:2] == "!":
                if find(letter[0]) == find(letter[3]):
                    return False
        return True