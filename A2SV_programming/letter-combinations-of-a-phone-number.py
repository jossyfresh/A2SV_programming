class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = defaultdict(list)
        c = 97
        for i in range(2,10):
            if i == 7 or i == 9:
                for j in range(4):
                    maps[i].append(chr(c))
                    c += 1
            else:
                for j in range(3):
                   maps[i].append(chr(c))
                   c += 1
        ans = set()
        def backtrack(i,arr):
            if i == len(digits):
                print(arr)
                if arr not in ans and arr:
                    ans.add(arr)
                return 
            for letter in maps[int(digits[i])]:
                backtrack(i+1,arr+letter)
            return 
        backtrack(0,"")
        return ans 


       