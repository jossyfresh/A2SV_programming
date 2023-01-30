class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        count = 1
        for r in range(1,len(chars)+1):

            if r < len(chars) and chars[r] == chars[r-1]:
                count+=1
            else:
                chars[l] = chars[r-1]
                l+=1
                if count > 1:
                    for x in str(count):
                        chars[l] = x
                        l+=1
                count = 1
        chars = chars[:l]
        return l
