class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        l = 0
        r = 0
        while l <len(word1) and r < len(word2):
            if ord(word1[l]) > ord(word2[r]):
                merge+=word1[l]
                l+=1
            elif ord(word2[r]) > ord(word1[l]):
                merge+=word2[r]
                r+=1
            else:
                n = l
                m = r
                flag = 0
                while n < len(word1) and m < len(word2):
                    if ord(word1[n]) > ord(word2[m]):
                        merge+=word1[l]
                        l+=1
                        flag = 1
                        break
                    elif ord(word1[n]) < ord(word2[m]):
                        merge+=word2[r]
                        r+=1
                        flag = 1
                        break
                    else:
                        n+=1
                        m+=1
                if flag  == 0:
                    if n == len(word1):
                        merge+=word2[r]
                        r+=1
                    else:
                        merge += word1[l]
                        l += 1
        while l < len(word1):
            merge+=word1[l]
            l+=1
        while r < len(word2):
            merge+=word2[r]
            r+=1
        return merge
