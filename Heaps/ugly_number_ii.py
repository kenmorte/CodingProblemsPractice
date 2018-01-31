# https://leetcode.com/problems/ugly-number-ii/description/

from heapq import heappop, heappush

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        seen = set()
        nums = [1]
        cnt = 0
        num = 0
        while cnt < n:
            num = heappop(nums)
            if num in seen: continue
            seen.add(num)
            cnt += 1
            heappush(nums, num*2)
            heappush(nums, num*3)
            heappush(nums, num*5)
        return num
