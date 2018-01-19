# https://leetcode.com/problems/partition-labels/description/

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        startIndex = {}
        endIndex = {}
        
        for i,c in enumerate(S):
            if c not in startIndex: startIndex[c] = i
            endIndex[c] = i
        
        intervals = sorted([(startIndex[c],endIndex[c]) for c in startIndex], key=lambda interval: interval[0])
        mergedIntervals = [intervals[0]]
        for interval in intervals[1:]:
            lastStart, lastEnd = mergedIntervals[-1]
            start, end = interval
            
            if lastStart <= start and start <= lastEnd: 
                mergedIntervals[-1] = (lastStart, max(lastEnd, end))
            else:
                mergedIntervals.append(interval)
                
        return [end-start+1 for start,end in mergedIntervals]
        
            
