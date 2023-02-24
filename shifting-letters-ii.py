class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = [0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                letters[shifts[i][0]] += 1
                letters[shifts[i][1]+1] -= 1
            else:
                letters[shifts[i][0]] -= 1
                letters[shifts[i][1]+1] += 1
        Sum = 0
        ans = ""
        for i in range(len(letters)):
            Sum+= letters[i]
            letters[i] = Sum
        print(letters)
        for i in range(len(letters)-1):
            asc = letters[i] % 26
            print(asc)
            if letters[i] < 0:
                ans+= chr(((ord(s[i])-97+asc)%26)+97)
            else:
                ans+= chr(((ord(s[i])-97+asc)%26)+97) 
        return ans