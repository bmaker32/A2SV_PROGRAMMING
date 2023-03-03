class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        temp = 0
        
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    while stack and stack[-1] != "(":
                        temp += stack.pop()
                        
                    if stack:
                        stack.pop()
                
                    if temp != 0 :
                        stack.append(2*temp)
                        temp = 0
                    else:
                        stack.append(1)  
             
        return sum(stack)
            
        