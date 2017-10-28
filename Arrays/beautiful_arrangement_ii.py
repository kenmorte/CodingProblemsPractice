# https://leetcode.com/problems/beautiful-arrangement-ii/description/

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n - k <= 0:
            return []
        
        factor = 1
        result = [1]
        current_k = k
        while current_k > 0:
            result.append(result[-1] + (current_k * factor))
            factor = -factor
            current_k -= 1
            
        return result + [n for n in range(k+2, n+1)]
