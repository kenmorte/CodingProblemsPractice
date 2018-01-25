# https://leetcode.com/problems/minimum-height-trees/description/

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {node:set() for node in xrange(n)}
        for edge in edges:
            node1, node2 = tuple(edge)
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        minHeight = float('inf')
        heights = {}
        res = []
        
        for node in xrange(n):
            maxHeight = self.maxHeight(node, graph, set(), heights)
            if maxHeight < minHeight: minHeight, res = maxHeight, [node]
            elif maxHeight == minHeight: res.append(node)
        return res
                
    
    def maxHeight(self, node, graph, visited, heights):
        visited.add(node)
        maxHeight = 0
        for child in graph[node]:
            if child not in visited:
                height = 0
                if (node, child) not in heights: 
                    heights[(node, child)] = self.maxHeight(child, graph, visited, heights)
                maxHeight = max(maxHeight, heights[(node, child)])
        visited.remove(node)
        return 1 + maxHeight
                
