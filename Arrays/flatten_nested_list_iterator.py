# https://leetcode.com/problems/flatten-nested-list-iterator/description/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.list = []
        self.index = 0
        for e in nestedList:
            self._flatten(e)

    def next(self):
        """
        :rtype: int
        """
        i = self.index
        self.index += 1
        return self.list[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.list)
        
    def _flatten(self, element):
        if element.isInteger(): self.list.append(element.getInteger())
        else: 
            for e in element.getList():
                self._flatten(e)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
