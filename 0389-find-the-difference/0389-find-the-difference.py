class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicts = {}
        dictt = {}
        output = ""
        for x in s:
            dicts[x]=dicts.get(x,0)+1
        for y in t:
            dictt[y]=dictt.get(y,0)+1
        for key in dictt:
            if key in dicts and dictt[key]==dicts[key]:
                dictt[key]=0
            elif key in dicts and dictt[key]>dicts[key]:
                dictt[key] = dictt[key]-dicts[key]
            else:
                continue
        for key in dictt:
            if dictt[key] > 0:
                str = key
                for i in range(dictt[key]):
                    output+=str
        return output