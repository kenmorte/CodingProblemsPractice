# https://leetcode.com/problems/replace-words/description/

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.trie = {'is_root': False}
        for root in dict:
            self.addTrie(root)
        
        new_sentence = []
        for word in sentence.split():
            newWord = self.getNewWord(word, self.trie, '')
            new_sentence.append(word if newWord is None else newWord)
        
        return ' '.join(new_sentence)
            
            
    def getNewWord(self, word, node, accumulatedRoot):
        if not word: return None
        if word[0] not in node: return None
        if node[word[0]]['is_root']: return accumulatedRoot + word[0]
        return self.getNewWord(word[1:], node[word[0]], accumulatedRoot + word[0])
        
    def addTrie(self, root):
        current_node = self.trie
        for c in root:
            if c not in current_node:
                current_node[c] = {'is_root': False}
            current_node = current_node[c]
        current_node['is_root'] = True
        
