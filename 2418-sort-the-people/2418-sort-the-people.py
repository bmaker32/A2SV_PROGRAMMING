class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:          
        
        for i in range(len(height)):
            mini = height[i]
            ind = i
            for j in range(i+1,len(height)):
                
                if mini < height[j]:
                    mini = height[j]
                    ind = j
            height[i],height[ind] = height[ind],height[i]
            names[i],names[ind] = names[ind],names[i]
        return names 
                
                