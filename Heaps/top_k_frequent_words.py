# https://leetcode.com/problems/top-k-frequent-words/description/

from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or not k: return []
        C = Counter(words)
        heap = []
        for word in C:
            heapq.heappush(heap, (C[word], word))
            # heapq.heappop(heap)
        d = {}
        while heap:
            count, word = heapq.heappop(heap)
            if count not in d: d[count] = []
            d[count] += [word]
        res = []
        for count in sorted(d, reverse=True): res += sorted(d[count])
        return res[:k]
