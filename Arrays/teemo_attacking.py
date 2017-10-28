# https://leetcode.com/problems/teemo-attacking/description/

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0 or duration == 0:
            return 0
        
        time = 0
        for i in range (len(timeSeries)-1):
            timePoisonFinishes = timeSeries[i] + duration
            if timePoisonFinishes > timeSeries[i+1]:
                time += timeSeries[i+1] - timeSeries[i]
            else:
                time += duration
        return time + duration
