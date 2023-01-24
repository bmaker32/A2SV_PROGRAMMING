class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while left < right:
            sumr =  numbers[left] + numbers[right]
            if (sumr) < target:
                left +=1
            elif (sumr) > target:
                right -= 1
            else:
                return [left+1,right+1]
                
            