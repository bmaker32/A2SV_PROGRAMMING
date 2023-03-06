class DataStream:

    def __init__(self, value: int, k: int):
        self.ds = [value,k]
        self.k = k
        self.value = value
        self.left = 0
        
        for i in range(len(self.ds)):
            if self.ds[i] != self.value:
                self.left = i
                break
        

    def consec(self, num: int) -> bool:       
        que = []
        check = 0
        
        self.ds.append(num) 
        
        if num != self.value:
            self.left = len(self.ds) - 1
        
        if len( self.ds) >= self.k:
            if ( (len(self.ds)-1) - self.left) >= self.k :
                return True
            else:
                return False
            
            
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)