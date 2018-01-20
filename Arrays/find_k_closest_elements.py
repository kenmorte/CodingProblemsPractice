# https://leetcode.com/problems/find-k-closest-elements/description/

from collections import deque

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        L, R, M = 0, len(arr), -1
        
        while L < R:
            M = (L+R)//2
            if arr[M] >= x: R = M
            else: L = M+1
        
        DQ = deque()
        
        if L > 0 and abs(x - arr[L-1]) <= abs(x - arr[L]): L -= 1
        R = L+1
        
        while k and L >= 0 and arr[L] == x:
            DQ.append(x)
            L -= 1
            k -= 1
        while k and R < len(arr) and arr[R] == x:
            DQ.append(x)
            R += 1
            k -= 1
        
        while k:
            if L < 0 and R >= len(arr): break
            k -= 1
            
            if L >= 0 and R < len(arr):
                Ldiff = abs(x - arr[L])
                Rdiff = abs(x - arr[R])
                
                if Ldiff <= Rdiff:
                    DQ.appendleft(arr[L])
                    L -= 1
                    
                else:
                    DQ.append(arr[R])
                    R += 1
                
            elif L < 0:
                DQ.append(arr[R])
                R += 1
                
            elif R >= len(arr):
                DQ.appendleft(arr[L])
                L -= 1
                
        return list(DQ)
        
