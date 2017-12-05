# https://leetcode.com/problems/gas-station/description/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost: return 0
        if len(gas) != len(cost): return 0
        d = [gas[i] - cost[i] for i in range(len(cost))]
        if sum(d) < 0: return -1
        res_i, res_sum = -1, float('-inf')
        start = d.index(min(d))
        if d[start] >= 0: return start
        i = self.findFirstPosFromHere(start, d)
        curr_i, curr_sum = i, d[i]
        start = i+1 if i < len(d)-1 else 0
        isPos = True
        while i != start:
            if d[i] >= 0:
                if isPos: curr_sum += d[i]
                else:
                    if curr_sum > res_sum: res_i = curr_i
                    curr_i = i
                    curr_sum = d[i]
                isPos = True
            else:
                isPos = False
                curr_sum += d[i]
            i = i+1 if i < len(d)-1 else 0
        if curr_sum > res_sum: res_i = curr_i
        return res_i
        
    def findFirstPosFromHere(self, i, a):
        if a[i] >= 0: return i
        for j in xrange(i+1,len(a)):
            if a[j] >= 0: return j
        for j in xrange(i):
            if a[j] >= 0: return j
        return -1
