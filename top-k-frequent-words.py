class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        heap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]