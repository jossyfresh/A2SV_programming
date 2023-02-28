class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tofinish = []
        cur = list(zip(position,speed))
        cur.sort()
        print(cur)
        for x in cur:
            time = float((target - x[0])/x[1])
            print(time)
            while tofinish and time >= tofinish[-1]:
                tofinish.pop()
            tofinish.append(time)
        return len(tofinish)