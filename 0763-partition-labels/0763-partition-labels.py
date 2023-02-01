class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={char:indx for indx,char in enumerate(s)}
        l=r=0
        res=[]
        
        for indx, char in enumerate(s):
            r = max(r,d[char])
            if r == indx:
                res.append(r-l+1)
                l=indx+1
        return res