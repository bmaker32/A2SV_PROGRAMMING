class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x_v_pair = [] 
        time = []
        ans = 0 
        for i in range(len(position)): 
            x_v_pair.append((position[i], speed[i])) 
        x_v_pair.sort() 
        x_v_pair.reverse() 
        for x, v in x_v_pair: 
            time.append((target - x) / v) 
        prev = 0 
        for cur in time: 
            if cur > prev: 
                ans += 1 
                prev = cur 
        return ans