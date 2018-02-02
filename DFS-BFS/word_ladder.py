# https://leetcode.com/problems/word-ladder/description/

from Queue import Queue

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList: return 0
        wordList.add(endWord)
        Q = Queue()
        self.addNext(beginWord, wordList, Q)
        res = 2
        while not Q.empty():
            n = Q.qsize()
            for _ in xrange(n):
                word = Q.get()
                if word == endWord: return res
                self.addNext(word, wordList, Q)
            res += 1
        return 0
                
    
    def addNext(self, word, wordList, Q):
        if word in wordList: wordList.remove(word)
        for i in xrange(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                test = word[:i] + c + word[i+1:]
                if test in wordList:
                    Q.put(test)
                    wordList.remove(test)
