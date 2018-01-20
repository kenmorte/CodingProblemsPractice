# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2,3,5,7,11,13,17,19}
        count = 0
        for n in xrange(L,R+1):
            if self.countSetBits(n) in primes: count += 1
        return count
    
    def countSetBits(self, n):
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count
