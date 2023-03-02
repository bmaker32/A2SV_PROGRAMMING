class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxim = max([e for _,_,e in trips]) 
        check = [0] * (maxim+2)

        for people,start,end in trips:
            check[start] += people
            if sum(check) > capacity:
                return False
            check[end] -= people
            
        prefix = list(accumulate(check))

        for i in prefix:
            if i > capacity:
                return False

        return True