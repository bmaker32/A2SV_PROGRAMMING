class Solution:
    def support(self,arr,l,r,turn):
        if l == r :
            if turn:
                return [arr[l],0]
            else:
                return [0,arr[l]]
        if turn:
            left = self.support(arr,l+1,r,not turn)
            left[0] += arr[l]
            right = self.support(arr,l,r-1,not turn)
            right[0] += arr[r]

            if left[0] >= right[0]:
                return left
            else:
                return right
        else:
            left = self.support(arr,l+1,r,not turn)
            left[1] += arr[l]
            right = self.support(arr,l,r-1,not turn)
            right[1] += arr[r]

            if left[1] >= right[1]:
                return left
            else:
                return right

        

    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.support(nums,0,len(nums)-1,True)

        return score[0] >= score[1]