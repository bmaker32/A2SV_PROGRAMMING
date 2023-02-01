class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        left = len(players) -1
        right = len(trainers)-1
        leng = min(len(players),len(trainers))
        players.sort()
        trainers.sort()
        count = 0
        
        while right >= 0 and left >= 0:
            print(players[left],trainers[right])
            if players[left] <= trainers[right]:
                count += 1
                right -= 1
                left -= 1
            else:
                left -= 1
                
        return count
    
    