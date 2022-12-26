class Solution:
    def interpret(self, command: str) -> str:
        stack =[]
        answer = ""
        for i in range(len(command)):
            if command[i] == ")":
                if stack and stack[-1] != "(":
                    answer+=str(command[i-2:i])
                    stack.pop()
                    stack.pop()
                elif stack and stack[-1] == "(":
                    answer+=str("o")
            elif command[i] == "G":
                answer+="G"
            else:    
                stack.append(command[i])
        return answer
        