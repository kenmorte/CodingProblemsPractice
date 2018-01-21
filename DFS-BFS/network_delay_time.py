# https://leetcode.com/problems/network-delay-time/description/

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {n:{} for n in xrange(1,N+1)}
        delay = {n:float('inf') for n in xrange(1,N+1)}        
        delay[K] = 0
        
        # Filling the graph
        for source, target, time in times: graph[source][target] = time
        
        # Start the Dijkstra on node K
        self.dijkstra(graph, K, set(), delay)
        res = max(delay.values())
        return res if res != float('inf') else -1
        
    def dijkstra(self, graph, node, visited, delay):
        for next in graph[node]: delay[next] = min(delay[next], delay[node] + graph[node][next])
        visited.add(node)
        
        nextNode = -1
        minDelay = float('inf')
        
        for next in delay:
            if next not in visited and delay[next] < minDelay:
                nextNode = next
                minDelay = delay[next]
        if nextNode > 0: self.dijkstra(graph, nextNode, visited, delay)
        
        
