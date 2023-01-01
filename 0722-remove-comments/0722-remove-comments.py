class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        check = True
        ans =[]
        code = ""
        comment = "/*"
        for line in source:
            i = 0
            x = 0
            len_ = len(line)
            while i < len_:
                if line[i] in comment:
                    if i+1 < len_ and line[i:i+2]=="//" and check == True:
                        x = 1
                        break
                    elif i+1 < len_ and line[i:i+2] == "/*" and check == True:
                        check = False
                        i+=2
                        continue
                    elif i+1 < len_ and line[i:i+2]== "*/" and check == False:
                        check = True
                        i+=2
                        continue
                if check == True :
                   code+=line[i]
                i+=1
            if code and check:
                ans.append(code)
                code = ""
        return ans
