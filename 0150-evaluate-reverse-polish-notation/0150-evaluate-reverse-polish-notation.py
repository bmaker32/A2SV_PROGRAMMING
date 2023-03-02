class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack2 = []

        for i in range(len(tokens)):
            var = tokens[i]
            
            if var == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif var == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif var == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif var == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if num1*num2 < 0:
                    # (a+(-a%b))//b
                    stack.append((num2+(-num2 % num1))//num1)
                else:
                    stack.append(num2//num1)
                
            else:
                stack.append(int(var))
            
        return stack[0]

            