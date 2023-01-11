
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        temp = []
        
        for j in range(len(words)):
                temp.append(list(words[j]))
        
        
        for i in temp[0]:
            check = True
            
            for j in range(1,len(temp)):
                
                if i not in temp[j]:
                    check = False
                else:
                    temp[j].pop(temp[j].index(i))
            if check == True: 
                ans.append(i)
        return ans
            
            