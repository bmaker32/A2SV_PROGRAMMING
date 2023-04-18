class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def permutation(s,i):
            if i ==(len(s)):
                output.append(s)
            for j in range(i,len(s)):
                s[i],s[j]=s[j],s[i]
                permutation(list(s),i+1)
                s[i],s[j]=s[j],s[i]
        permutation(nums,0)
        return(output)