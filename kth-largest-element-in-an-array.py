class Solution:
    def mergesort(self,arrone,arrtwo):
            ans = []

            while arrone and arrtwo:
                
                if arrone[0] > arrtwo[0]:
                    ans.append(arrtwo[0])
                    arrtwo.remove(arrtwo[0])
                else:
                    ans.append(arrone[0])
                    arrone.remove(arrone[0])
            print("crude",ans)
            ans.extend(arrtwo)
            ans.extend(arrone)
            return ans

    def merge(self,arr,left,right):
            if left >= right:
                return arr
            # [2,3,4,5,6,7,8,9]

            

            mid = left + (right-left)//2

            arrone = self.merge(arr,left,mid)
            arrtwo = self.merge(arr,mid+1,right)

            return self.mergesort(arrone,arrtwo)

    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        # ans = self.merge(nums,0,len(nums)-1)
        
        # print(ans)
        nums.sort(reverse = True)
        return nums[k-1]