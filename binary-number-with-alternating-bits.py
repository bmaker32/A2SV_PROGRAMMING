class Solution(object):
    def hasAlternatingBits(self, n):
        num = ""
        i = -1
        while n != 0:
            i += 1
            s = n & 1
            n >>= 1
            num += str(s)
            if len(num) >= 2:
                if num[i - 1] == num[i]:
                    return False
        return True