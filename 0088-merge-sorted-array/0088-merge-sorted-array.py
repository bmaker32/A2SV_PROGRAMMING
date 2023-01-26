import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = len(nums1) - 1
        right= 0
        
        while left < len(nums1) and nums1[left] == 0 and right < len(nums2):
            
            nums1[left] = nums2[right]
            right += 1
            left -= 1
        nums1.sort()
        
            
                
            
        