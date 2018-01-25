# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.trie
        for c in word:
            if c not in root.children: root.children[c] = TrieNode()
            root = root.children[c]
        root.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.wordExistsFromRoot(word, self.trie)
            
    def wordExistsFromRoot(self, word, root):
        for i, c in enumerate(word):
            if c == '.': return any(self.wordExistsFromRoot(word[i+1:], root.children[c]) for c in root.children)
            if c not in root.children: return False
            root = root.children[c]
        return root.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
