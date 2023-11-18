class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dp(op,cl,word):
            if op == n and cl == n:
                ans.append("".join(word))
                return 1
            a = 0
            b = 0
            c = 0
            if op == n:
                a = dp(op,cl + 1,word + [")"])
            else:
                if op > cl:
                    b = dp(op,cl+1,word + [")"]) + dp(op+1,cl,word + ["("])
                else:
                    c = dp(op+1,cl,word + ["("])
            return a + b + c
        dp(0,0,[])
        return ans
