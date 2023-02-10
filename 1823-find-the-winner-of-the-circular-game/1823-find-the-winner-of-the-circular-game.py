class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        ind = 0
        li=[]
        for i in range(n):
            li.append(i+1)
        li.sort()
        count = len(li)-1
        
        while len(li) > 1:
            count = (count  + k ) % len(li)
            print(count,li[count])
            li.remove(li[count])
            count -= 1
        return int(li[0])
                
            