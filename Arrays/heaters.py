# https://leetcode.com/problems/heaters/description/

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = float('-inf')
        heaters.sort()
        for house in houses:
            L, R = 0, len(heaters)-1
            while L < R:
                M = (L+R)//2
                if house <= heaters[M]: R = M
                else: L = M+1
            closestHeaterDist = min(abs(house-heaters[L]), float('inf') if not L > 0 else abs(house-heaters[L-1]))
            res = max(res, closestHeaterDist)
        return res
