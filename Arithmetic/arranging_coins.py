# https://leetcode.com/problems/arranging-coins/description/

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        cnt = 0
        while n >= k:
            n -= k
            cnt += 1
            k += 1
        return cnt
