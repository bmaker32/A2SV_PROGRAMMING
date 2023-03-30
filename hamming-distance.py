class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        return temp.bit_count()