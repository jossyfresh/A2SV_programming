class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        power1 =len(num1)-1
        power2 = len(num2)-1
        x = 0
        y = 0
        for i in num1:
            num = int(i)*10**power1
            x+=num
            power1-=1
        for i in num2:
            num =int(i)*10**power2
            y+=num
            power2-=1
        ans = x*y
        return str(ans)
        
                