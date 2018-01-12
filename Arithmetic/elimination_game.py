# https://leetcode.com/problems/elimination-game/description/

class Solution(object):
    def lastRemaining(self, n):
        if n <= 1: return 1
        head, step, remaining, removeFromLeft = 1, 1, n, True
        while remaining > 1:
            if removeFromLeft or remaining % 2 == 1: head += step
            remaining /= 2
            step *= 2
            removeFromLeft = not removeFromLeft
        return head
        
    
    def lastRemainingFirstSolution(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return -1
        if n == 1: return 1
        minN, maxN, step = 1, n, 2
        S = {num for num in xrange(1,n+1)}
        removeFromLeft = True
        while len(S) != 1:
            iterator = xrange(minN,maxN+1,step) if removeFromLeft else xrange(maxN,minN-1,-step)
            for i in iterator:
                S.remove(i)
            minN = min(S)
            maxN = max(S)
            step *= 2
            removeFromLeft = not removeFromLeft
        return list(S)[0]
