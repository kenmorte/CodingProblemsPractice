# https://leetcode.com/problems/jewels-and-stones/description/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        cnt = 0
        for c in S: cnt += 1 if c in J else 0
        return cnt
