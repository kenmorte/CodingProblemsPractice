# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import deque

class Solution(object):
    def subarraySum(self,A,k):
        if not A: return 0
        prefixSum = {0:1}
        currSum = 0
        res = 0
        for n in A:
            currSum += n
            if currSum - k in prefixSum:
                res += prefixSum[currSum - k]
            if currSum not in prefixSum: prefixSum[currSum] = 0
            prefixSum[currSum] += 1
        return res
    
    def subarraySumFirstSolution(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not A: return 0
        DQ, curr_sum, res = deque(), 0 , set()
        if sum(A) == k: res.add((0,len(A)-1))
        for i, n in enumerate(A):
            DQ.append((i,n))
            curr_sum += n
            if curr_sum == k: 
                res.add((DQ[0][0], i))
                if not DQ: continue
            
                stack = [DQ.popleft()]
                curr_sum -= stack[0][1]
                while curr_sum == k and DQ:
                    res.add((DQ[0][0], i))
                    stack.append(DQ.popleft())
                    curr_sum -= stack[-1][1]
                while stack: 
                    popped = stack.pop()
                    curr_sum += popped[1]
                    DQ.appendleft(popped)
                    
                
            elif curr_sum > k:
                while curr_sum > k and DQ:
                    curr_sum -= DQ.popleft()[1]
                    if curr_sum == k and DQ: res.add((DQ[0][0], i))
                if not DQ: continue
                        
                stack = [DQ.popleft()]
                curr_sum -= stack[0][1]
                while curr_sum == k and DQ:
                    res.add((DQ[0][0], i))
                    stack.append(DQ.popleft())
                    curr_sum -= stack[-1][1]
                while stack: 
                    popped = stack.pop()
                    curr_sum += popped[1]
                    DQ.appendleft(popped)
            print DQ, curr_sum
                    
        while DQ:
            curr_sum -= DQ.popleft()[1]
            if curr_sum == k and DQ: 
                res.add((DQ[0][0], i))
                    
        return len(res)
