class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.m = {times[0]:persons[0]}
        self.person = persons
        self.times = times
        for i in range(1,len(persons)):
            d = Counter(persons[:i+1])
            x = max(d,key = d.get)
            if d[persons[i]] == d[x]:
                self.m[times[i]] = persons[i]
            else:
                j = i-1
                while j >= 0:
                    if d[persons[j]] == d[x]:
                        self.m[times[i]] = persons[j]
                        break
                    j-=1      
    def q(self, t: int) -> int:
        return self.m[self.times[bisect_right(self.times,t)-1]]
        
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)