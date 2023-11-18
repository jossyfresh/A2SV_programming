class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        maps = {chr(i+97):i+1 for i in range(26)}
        for y in strs:
            c = []
            x = Counter(y)
            for i in x:
                c.append(i + str(x[i]))
            c.sort()
            c = tuple(c)
            dict[tuple(c)].append(y) 
        ans = []   
        for x in dict:
            res = []
            for word in dict[x]:
                res.append(word)
            ans.append(res)
        return ans
