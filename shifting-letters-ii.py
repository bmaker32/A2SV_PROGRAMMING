class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0]*(len(s) + 1) 

        s = [ord(i)-ord("a") for i in s]

        for i in range(len(shifts)):
            if shifts[i][2]:
                temp[shifts[i][0]] += 1
                temp[shifts[i][1] + 1] -= 1
            else:
                temp[shifts[i][0]] -= 1
                temp[shifts[i][1] + 1] += 1
       

        temp = list(accumulate(temp))
        print(temp)

        j = 0
        for i in range(len(temp)-1):
            s[i]= (s[i] + temp[j] + 26) % 26
            print(s[i])
            j += 1
            
        s = [chr(i + ord("a")) for i in s]

        return "".join(s)