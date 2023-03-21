class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        sec = 0
        while True:
            if tickets[i] != 0:
                tickets[i]-=1
                sec+=1
            
            if tickets[k] == 0:
                return sec
            if i == len(tickets)-1:
                i = 0
            else:
                i+=1