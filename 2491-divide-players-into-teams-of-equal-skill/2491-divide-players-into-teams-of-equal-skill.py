class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        right = len(skill)-1
        left = 0
        le = len(skill)
        skill.sort()
        com = skill[left] + skill[right]
        mul = 0
#         [1,2,3,3,4,5]
        
        while left < right :
            
            
            if com == (skill[left]+skill[right]):
                
                mul = mul + (skill[left]*skill[right])
                right -= 1
                left += 1
            else:
                return -1
        return mul
            
            
    