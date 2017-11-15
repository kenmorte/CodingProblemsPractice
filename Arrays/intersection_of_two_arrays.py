# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution(object):
    def intersect(self, n1, n2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not n1 or not n2: return []
        m1,m2 = {},{}
        for n in n1:
            if n not in m1: m1[n] = 0
            m1[n] += 1
        for n in n2:
            if n not in m2: m2[n] = 0
            m2[n] += 1
        res = []
        for n in m1:
            if n in m2:
                o = min(m1[n],m2[n])
                res += [n for _ in range(o)]
        return res
