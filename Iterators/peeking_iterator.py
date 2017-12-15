# https://leetcode.com/problems/peeking-iterator/description/

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.hasNextBool = iterator.hasNext()
        self.currVal = iterator.next() if self.hasNext else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.currVal

    def next(self):
        """
        :rtype: int
        """
        res = self.currVal
        self.hasNextBool = self.it.hasNext()
        self.currVal = self.it.next()
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasNextBool

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
