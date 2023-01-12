class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        diction = {}
        for x in words[0]:
            diction[x] = diction.get(x,0)+1
        letter = []
        for i in range(1, len(words)):
            for x in diction:
                if diction[x] > 1:
                    if x in words[i]:
                        diction[x] = min(diction[x],words[i].count(x))
                if x not in words[i]:
                    letter.append(x)      
        ans = []
        for i in diction:
            if i not in letter:
                for j in range(diction[i]):
                    ans.append(i)
                    
        return ans
        