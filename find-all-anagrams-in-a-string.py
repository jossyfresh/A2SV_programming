class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        window = {}
        for x in p:
            target[x] = target.get(x,0)+1
        if len(p) <= len(s):
            for i in range(len(p)):
                window[s[i]] = window.get(s[i],0)+1
                print(s[i])
            print(target)
            print(window)
            count = []
            k = len(p)
            l = 0
            while k < len(s):
                if window == target:
                    count.append(l)
                window[s[k]] = window.get(s[k],0)+1
                if window[s[l]] > 1:
                    window[s[l]] = window.get(s[l],0)-1
                else:
                    window.pop(s[l])
                k+=1
                l+=1
            if target == window:
                count.append(l)
            return count
        else:
            return []