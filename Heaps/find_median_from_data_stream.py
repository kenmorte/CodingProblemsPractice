# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap, self.maxHeap, self.median = [], [], None

    def addNum(self, n):
        """
        :type num: int
        :rtype: void
        """
        if not self.minHeap and not self.maxHeap:
            self.maxHeap.append(-n)
            self.median = n
            return
        if n <= self.median: heapq.heappush(self.maxHeap, -n)
        else: heapq.heappush(self.minHeap, n)
        
        if len(self.maxHeap) == len(self.minHeap)+2:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        self.median = -self.maxHeap[0] if (len(self.maxHeap) + len(self.minHeap))%2 == 1 else (-self.maxHeap[0]+self.minHeap[0])/2.0

    def findMedian(self):
        """
        :rtype: float
        """
        return float(self.median)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
