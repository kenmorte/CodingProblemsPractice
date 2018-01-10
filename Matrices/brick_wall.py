# https://leetcode.com/problems/brick-wall/description/

class Solution(object):
    def leastBricks(self, W):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not W: return 0
        G = {}
        for r in W:
            gap = r[0]
            if gap not in G: G[gap] = 0
            G[gap] += 1
            for b in r[1:len(r)-1]:
                gap += b
                if gap not in G: G[gap] = 0
                G[gap] += 1
        if len(G) == 1: return len(W)
        return len(W) - max(G.values())
