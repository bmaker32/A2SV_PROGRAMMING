class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = list(accumulate(nums,operator.mul))
        
        nums.reverse()
        ans = []
        
#         postfix = list(accumulate(nums,operator.mul))
#         postfix.sort(reverse=True)
        
#         print(postfix,prefix)
        
        postfix = []
        
        
        
        for i in range(len(nums)):
            if postfix == []:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[-1]*nums[i])
        print(postfix)
        postfix.reverse()
        
        
        
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[i+1])
            elif i == len(nums)-1:
                ans.append(prefix[i-1])
            else:
                print(prefix[i-1],postfix[i+1],i)
                ans.append(prefix[i-1] * postfix[i+1])
        
        
        
            
        return ans
            
            
        