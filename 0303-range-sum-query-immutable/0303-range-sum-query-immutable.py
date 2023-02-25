class NumArray:

    def __init__(self, nums: List[int]):
        self.acum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.acum[right + 1] - self.acum[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)