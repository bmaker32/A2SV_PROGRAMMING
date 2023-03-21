class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        j=0
        ck=True
        try:
            val=nums.index(target)
        except :
            val=None
        if val is not None:
            ck=False
            j=nums.count(target)
            return [val,val+j-1]
        if ck==True:
            return [-1,-1]