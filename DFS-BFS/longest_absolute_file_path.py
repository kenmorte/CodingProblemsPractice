class Node:
    def __init__(self, name, isFile):
        self.name = name
        self.isFile = isFile
        self.children = set()

class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen 
    
    def lengthLongestPathFirstSolution(self, input):
        """
        :type input: str
        :rtype: int
        """
        topNodes = self.pathToGraph(input.replace('    ','\t'))
        res = 0
        for node in topNodes:
            res = max(res, self.dfs(node, 0))
        return max(res, 0)
        
    def pathToGraph(self, path):
        if not path: return
        path = path.split('\n')
        if self.isFile(path[0]): return [Node(path[0], True)]
        stack = [(Node(path[0], False),0)]
        res = []
        for val in path[1:]:
            level = self.getLevel(val)
            while stack and level <= stack[-1][1]: 
                popped = stack.pop()
                if not popped[1]: res.append(popped[0])
            name = self.getName(val)
            if stack and level - stack[-1][1] > 1:
                level = stack[-1][1]
            node = Node(name, self.isFile(name))
            if stack: stack[-1][0].children.add(node)
            if not node.isFile: stack.append((node, level))
        return res + [t[0] for t in stack if not t[1]]
    
    def dfs(self, root, length):
        if not root: return 0
        if root.isFile: return length + len(root.name)
        res = float('-inf')
        for node in root.children:
            res = max(res, self.dfs(node, length + len(root.name) + 1))
        return res
    
    def getLevel(self, node):
        if '\t' in node: return node.count('\t')
        return node.count('    ')
    
    def getName(self, node):
        if '\t' in node: return node.split('\t')[-1]
        return node.lstrip()
        
    def isFile(self, node):
        return '.' in node
