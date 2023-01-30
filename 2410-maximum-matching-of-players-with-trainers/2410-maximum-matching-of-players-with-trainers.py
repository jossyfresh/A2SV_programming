class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l  = 0
        r = 0
        count = 0
        while l < len(players) and r < len(trainers):
            if trainers[r] >= players[l]:
                count+=1
                l+=1
                r+=1
            else:
                r+=1
        return count