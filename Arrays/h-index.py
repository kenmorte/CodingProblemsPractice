# https://leetcode.com/problems/h-index/description/

class Solution(object):
    def hIndex(self, citations):
        if not citations: return 0
        buckets = [0 for _ in xrange(len(citations)+1)]
        for citation in citations: buckets[(min(len(citations),citation))] += 1
        count = 0
        for hIndex in xrange(len(citations),-1,-1):
            count += buckets[hIndex]
            if count >= hIndex: return hIndex
    
    def hIndexFirstSolution(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        citations.sort()
        if citations[-1] == 0: return 0
        res = -1
        for i in xrange(len(citations)-1,-1,-1):
            citation = citations[i]
            hIndex = len(citations) - i
            
            if hIndex > citation: break
            res = hIndex
        return res
