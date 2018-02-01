# https://leetcode.com/problems/all-oone-data-structure/description/

class DoublyLinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valuesDict = {}
        self.maxDict = {}
        self.minDict = {}
        self.minNodes = {}
        self.minHead = self.minTail = None
        self.minVal = float('inf')
        self.maxVal = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # Update values dict
        if key not in self.valuesDict: self.valuesDict[key] = 0
        originalValue = self.valuesDict[key]
        self.valuesDict[key] += 1
        currentValue = self.valuesDict[key]
        
        # Update max values/dict
        if currentValue not in self.maxDict: self.maxDict[currentValue] = set()
        self.maxVal = max(self.maxVal, currentValue)
        self.maxDict[currentValue].add(key)
        
        # Update min values/dict
        if not self.minDict: self._initMinDict(key)
        else: self._upateMinDict(originalValue, currentValue, key)

        # self.printLinkedList()

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.valuesDict: return
        
        originalValue = self.valuesDict[key]
        self.valuesDict[key] -= 1
        currentValue = self.valuesDict[key]
        if not currentValue: del self.valuesDict[key]
        
        # Update the max dict
        self.maxDict[originalValue].remove(key)
        if not self.maxDict[originalValue]: 
            del self.maxDict[originalValue]
            self.maxVal -= 1
        
        # Update the min dict
        self._upateMinDict(originalValue, currentValue, key)
        # self.printLinkedList()
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.maxDict: return ''
        for key in self.maxDict[self.maxVal]: return key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.minDict or self.minVal == float('inf'): return ''
        for key in self.minDict[self.minVal]: return key
        
    def _initMinDict(self, key):
        self.minDict[1] = {key,}
        self.minVal = 1
        self.minHead = self.minTail = DoublyLinkedListNode(1)
        self.minNodes[1] = self.minHead
        
    def _upateMinDict(self, originalValue, currentValue, key):
        if originalValue: 
            self.minDict[originalValue].remove(key)
            if not self.minDict[originalValue]:
                del self.minDict[originalValue]
                self._deleteNode(originalValue)
        self.minVal = float('inf') if not self.minHead else self.minHead.val
        if currentValue: 
            if currentValue not in self.minDict:
                self.minDict[currentValue] = set()
                if currentValue > self.minVal: self._addNodeRight(currentValue)
                elif currentValue < self.minVal: self._addNodeLeft(currentValue)
            self.minDict[currentValue].add(key)
            # print 'current value = ', currentValue, 'min val = ', self.minVal, self.minDict
        self.minVal = float('inf') if not self.minHead else self.minHead.val
        
    def _addNodeLeft(self, value):
        node = DoublyLinkedListNode(value)
        node.right = self.minHead
        if self.minHead: self.minHead.left = node
        self.minHead = node
        self.minNodes[value] = node
    
    def _addNodeRight(self, value):
        node = DoublyLinkedListNode(value)
        node.left = self.minTail
        if self.minTail: self.minTail.right = node
        self.minTail = node
        self.minNodes[value] = node
    
    def _deleteNode(self, value):
        node = self.minNodes[value]
        if node == self.minHead and node == self.minTail: self.minHead = self.minTail = None
        elif node == self.minHead:
            right = node.right
            if right: right.left = None
            self.minHead = right
            if self.minHead and not self.minHead.right: self.minTail = self.minHead
        elif node == self.minTail:
            self.minTail = node.left
            if self.minTail: self.minTail.right = None
        else:
            left = node.left
            right = node.right
            if left: left.right = right
            if right: right.left = left
            
    def printLinkedList(self):
        curr = self.minHead
        if not curr: print 'null'
        while curr:
            print str(curr.val) + '->',
            curr = curr.right
        print ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
