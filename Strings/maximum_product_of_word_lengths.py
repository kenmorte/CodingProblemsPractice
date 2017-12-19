# https://leetcode.com/problems/maximum-product-of-word-lengths/description/

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        setWords = [set(word) for word in words]
        res = 0
        for i in xrange(len(setWords)):
            for j in xrange(i+1,len(setWords)):
                cancel = False
                for c in setWords[i]:
                    if c in setWords[j]:
                        cancel = True
                        break
                if not cancel: res = max(res, len(words[i]*len(words[j])))
        return res
