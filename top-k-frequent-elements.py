class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        array = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1
        
        for key in hash_map:
            array.append(key)
        
        def quick_sort(i, j, k):
            if i >= j:
                return
        
            mid = i + (j - i) // 2
            array[mid], array[j] = array[j], array[mid]
            curr = i

            for idx in range(i, j):
                if hash_map[array[idx]] >= hash_map[array[j]]:
                    array[idx], array[curr] = array[curr], array[idx]
                    curr += 1
            array[curr], array[j] = array[j], array[curr]
            
            if curr < i + k:
                quick_sort(curr + 1, j, k - (curr - i))
            elif curr > i + k:
                quick_sort(i, curr - 1, k)
            else:
                return
        
        quick_sort(0, len(array) - 1, k)

        return array[:k]