class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        le = 0
        count = 0
        ans = []
        for i in range(len(strs)):
            strs[i] = list(strs[i])
        
        while le < len(strs[0]):
            temp = []
            for i in range(len(strs)):
                temp.append(strs[i][le])
            print("temp: ",temp)
            temp1 = temp[:]
            temp1.sort()
            if  temp != temp1:
                # print("annoying little shit")
                # for i in range(len(strs)):
                #     strs[i].pop(strs.index(strs[i][le]))
                count += 1
            le += 1
        return count
            