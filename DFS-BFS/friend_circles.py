# https://leetcode.com/problems/friend-circles/description/


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.graph = dict()
        self.visited = set()
        friend_groups = list()
            
        # Create adjacency list
        for i in range(len(M)):
            self.graph[i] = set()
            for j in range(len(M[i])):
                if i == j: continue
                if M[i][j]: self.graph[i].add(j)
            
        for node in self.graph:
            if node not in self.visited:
                friend_group = set()
                if len(self.graph[node]) > 0:
                    self.visit(node, friend_group)
                else:
                    friend_group = {node}
                friend_groups.append(friend_group)
        print self.graph
        print friend_groups
        return len(friend_groups)
    
    def visit(self, node, friend_group):
        if node in self.visited: return
        friend_group.add(node)
        self.visited.add(node)
        for sub_node in self.graph[node]:
            self.visit(sub_node, friend_group)
        
