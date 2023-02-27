class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxim = 0
        bas2 = {}
        
        left = 0
      
        
        
        for right in range(len(fruits)):
            
            bas2[fruits[right]] = bas2.get(fruits[right],0) + 1
            
            while len(bas2) > 2:
                
                bas2[fruits[left]] -= 1
                
                if bas2[fruits[left]] == 0:
                    del bas2[fruits[left]]
                left += 1
            maxim = max(maxim, right-left+1)
        
        return maxim        
                
            
        
#         while i < len(fruits):
#             if bas1 == [] or fruits[i] in bas1:
#                 bas1.append(fruits[i])
#             elif bas2 == []:
#                 bas2.append(fruits[i])
            
#             if fruits[i] not in bas1 and fruits[i] not in bas2:
#                 print(bas1,bas2)
#                 maxim = max(maxim, (len(bas1)+len(bas2)))
#                 bas2 = []
#                 bas1 = []
#                 left += 1
#             else:
#                 print(bas1,bas2)
#             i += 1
#         else:
#             print(bas1,bas2)
#             maxim = max(maxim, (len(bas1)+len(bas2)))
#             bas2 = []
#             bas1 = []
            
                
        
                
            
                
                