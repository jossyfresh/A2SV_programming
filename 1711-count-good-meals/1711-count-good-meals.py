class Solution:
    def countPairs(self, deli: List[int]) -> int:
        import math
        dict = {}
        count = 0
        for x in deli:
            dict[x] = dict.get(x,0)+1
        print(dict)
        for x in deli:
            if x in dict:
                for i in range(22):
                    val = (2 ** i) - x
                    if val in dict and val == x:
                        if dict[x] > 1:
                            count+=(math.factorial(dict[x]))/(math.factorial(dict[x]-2)*2)
                    elif val in dict and val!=x:
                        count+=dict[val]* dict[x]
                    else:
                        continue
                dict.pop(x)
        ans = int(count)
        return ans % 1_000_000_007
