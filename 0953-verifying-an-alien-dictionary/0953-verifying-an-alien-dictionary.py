class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words=list(words)
        for i in range(len(words)):
            words[i] = list(words[i])
        
        for i in range(len(words)):
            for k in range(len(words[i])):
                for j in range(len(order)):
                    if words[i][k] == order[j]:
                        words[i][k]=j
        for i in range(1,len(words)):
            if words[i-1] > words[i]:
                return False
        return True
        
        
        # for i in range(len(words)):
        #     for k in range(len(words[i])):
        #         if i < len(words)-1  and len(words[i+1]) > k:
        #             if words[i][k] > words[i+1][k]:
        #                 return False
        
              
        # print(words)
        # return True
             