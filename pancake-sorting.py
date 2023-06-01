class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        for n in range(len(arr), 1, -1):
            maxIndex = arr.index(max(arr[:n]))
            if maxIndex != n - 1:
                if maxIndex != 0:
                    result.append(maxIndex + 1)
                    arr[:maxIndex + 1] = reversed(arr[:maxIndex + 1])
                result.append(n)
                arr[:n] = reversed(arr[:n])
        return result