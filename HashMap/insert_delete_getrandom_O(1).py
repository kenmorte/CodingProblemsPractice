# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 1000
        self.hashTable = [[] for i in range(self.length)]
        self.validIndices = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        hashIndex = val % self.length
        hashBucket = self.hashTable[hashIndex]
        if val not in hashBucket: 
            hashBucket.append(val)
            if hashIndex not in self.validIndices: self.validIndices.append(hashIndex)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        hashIndex = val % self.length
        hashBucket = self.hashTable[hashIndex]
        if val in hashBucket:
            hashBucket.remove(val)
            if not hashBucket: self.validIndices.remove(hashIndex)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomHashIndex = random.choice(self.validIndices)
        hashBucket = self.hashTable[randomHashIndex]
        return random.choice(hashBucket)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
