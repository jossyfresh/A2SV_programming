class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict = {}
        for i,x in enumerate(arr):
            if x!=2 and x!=0:
                dict[x] = i
            elif x == 2 and x not in dict:
                dict[x] = str(i)
            elif x == 0 and x not in dict:
                dict[x] = str(i)
            elif x == 2 and x in dict:
                dict[x] = dict.get(x,0)+"#"+str(i)
            elif x == 0 and x in dict:
                dict[x] = dict.get(x, 0) + "#" + str(i)
        for x in dict:
            if x == 2 or x == 0:
                s = str(dict[x])
                x = s.split("#")
                if len(x)>1 and 4 in dict or len(x) > 1 and 0 in dict:
                    return True
            elif x/2 in dict:
                return True
            
        return False
                
                
            