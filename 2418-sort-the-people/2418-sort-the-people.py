class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        
        for j in range( len( heights)-1):
            for i in range( len(heights)-j-1):
                if  heights[i + 1] > heights[i]:
                    heights[i + 1],heights[i] = heights[i], heights[i + 1]
                    names[ i + 1 ], names[i] = names [i], names[ i + 1]
        print(heights)
                
        return names
                