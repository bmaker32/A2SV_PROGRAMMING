class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        
        counter = Counter(s1) 
        counter2 = {}
        left = 0
        
        for right in range(len(s2)):
            counter2[s2[right]] = counter2.get(s2[right],0) + 1 
            
            while (right - left + 1) == size:
                if counter == counter2:
                    return True
                counter2[s2[left]] -= 1
                if counter2[s2[left]] == 0:
                    del counter2[s2[left]]
                left += 1
        return False
            
                
            
        
         