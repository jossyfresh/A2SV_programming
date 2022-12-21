class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        for word in strs:
            if len(check)>len(word):
                check = word                    
        for x in strs:
            size = min(len(x),len(check))
            for i in range(size):
                if x[i]==check[i]:
                    continue
                else:
                    check = check[0:i]
                    break
                check = check[0:i]
        return check