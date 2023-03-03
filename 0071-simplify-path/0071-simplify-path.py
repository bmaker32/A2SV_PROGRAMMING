class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        
        stack = []       
        
        for char in paths:
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
                
        stack = "/".join(stack)
        stack = "/" + stack
       
        return stack
                
        
                
                