class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """        
        n = len(arr)
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                break
        else:
            return arr
        for j in range(n-1, i, -1):
            if arr[j] < arr[i]:
                break
        while arr[j] == arr[j-1]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr