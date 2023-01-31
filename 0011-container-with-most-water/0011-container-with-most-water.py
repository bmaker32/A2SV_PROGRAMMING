class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = -1
        left = 0
        right = len(height) - 1
        
        while left < right:
            num = min(height[left],height[right])
            area = num * (right - left)
            print(left,right,ma)
            ma = max(ma,area)
            print(num)
            if (height[left]<height[right]):
                left += 1
            else:
                right -= 1
        return ma
        