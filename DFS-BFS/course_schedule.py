# https://leetcode.com/problems/course-schedule/description/

class Solution(object):
    def canFinish(self, n, prereqs):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if n==0 or not prereqs: return True
        t, g = {i for i in xrange(n)}, {}
        for p in prereqs:
            x, y = tuple(p)
            if x==y: continue
            if x in t: t.remove(x)
            if y not in g: g[y] = set()
            g[y].add(x)
        if not t: return False
        v = set()
        has_cycle = False
        for node in t: 
            if self.dfs(node, g, v, set()): return False
        return len(v) == n and not has_cycle
    
    def dfs(self, n, g, v, currPath):
        if n in currPath: 
            print 'has cycle'
            currPath.remove(n)
            return True
        v.add(n)
        has_cycle = False
        if n not in g: return
        currPath.add(n)
        for nn in g[n]:
            if nn not in currPath:
                if self.dfs(nn, g, v, currPath): 
                    return True
            else: return True
        currPath.remove(n)
        return has_cycle
