# https://leetcode.com/problems/map-sum-pairs/description/

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        current_node = self.trie
        for c in key:
            if c not in current_node:
                current_node[c] = {'value': 0}
            current_node = current_node[c]
        current_node['value'] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current_node = self.trie
        for c in prefix:
            if c not in current_node: # Prefix is not in our tree
                return 0
            current_node = current_node[c]
        
        # Current node should be at the end of the prefix, we have to sum up all value from this prefix
        return self.traverse(current_node, 0)
    
    def traverse(self, node, result):
        result += node['value']
        for c in node:
            if c != 'value':
                result = self.traverse(node[c], result)
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
