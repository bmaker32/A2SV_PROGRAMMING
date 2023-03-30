class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        counter = 0

        while num :
            temp = not (num & 1)
            num = num >> 1
            temp = temp << counter
            ans += temp
            counter += 1
        return (ans)