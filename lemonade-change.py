class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for x in bills:
            if x == 5:
                five += 1
            else:
                if x == 10:
                    if five > 0:
                        five -= 1
                        ten += 1
                    else:
                        return False
                elif x == 20:
                    if ten > 0 and five > 0:
                        ten -= 1
                        five -= 1
                    else:
                        if five > 2:
                            five -= 3
                        else:
                            return False
        return True