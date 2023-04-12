class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mapping = {}

        for x in deck:
            mapping[x] = mapping.get(x, 0) + 1
        
        div = 2
        while div <= min(mapping.values()):
            if not [x for x in mapping.values() if x % div]:
                return True
            
            div += 1
        
        return False