class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        right = len(people) -1 
        left = 0 
        boats = 0
        people.sort()
        print(people)
        
        while left <= right:
            print(people[right],people[left])
            if (people[left]+people[right]) <= limit:
                boats += 1
                left += 1
                right -= 1
            elif people[left] == limit:
                print("left")
                boats += 1
                left += 1
            else:
                print("right")
                boats +=1
                right -=1 
        return boats 
                
            