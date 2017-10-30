# https://leetcode.com/problems/implement-magic-dictionary/description/

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self._addToDict(word)
        
    def _addToDict(self, word):
        current_node = self.trie
        for c in word:
            if c not in current_node:
                current_node[c] = {'isWord': False}
            current_node = current_node[c]
        current_node['isWord'] = True
        
    def traverseTrie(self, word, node, hasModifiedOneChar):
        if not word:
            return hasModifiedOneChar and node['isWord']
        if not node:
            return False
        
        currentChar = word[0]
        # print 'word = ', word, 'word[1:] = ', word[1:], 'node = ', node, 'hasModifiedOneChar = ', hasModifiedOneChar
        
        # Traverse through child nodes to see if we can go through entire word only needing to replace one char
        for char in node:
            if char == 'isWord':
                continue
            
            charNeedsToBeReplaced = currentChar != char
            # print '\tcurrentChar = ', currentChar, 'char = ', char
            
            if hasModifiedOneChar:
                if not charNeedsToBeReplaced and self.traverseTrie(word[1:], node[char], True):
                    return True
            else:
                if self.traverseTrie(word[1:], node[char], charNeedsToBeReplaced):
                    return True
        return False
                
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        print 'Searching: ', word
        return self.traverseTrie(word, self.trie, False)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
