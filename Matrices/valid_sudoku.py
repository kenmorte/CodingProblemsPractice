# https://leetcode.com/problems/valid-sudoku/description/

class Solution(object):
    def isValidSudoku(self, b):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {(i,j):set() for i in xrange(3) for j in xrange(3)}
        h = {i:set() for i in xrange(9)}
        v = {j:set() for j in xrange(9)}
        for i in xrange(9): print b[i]

        for i in xrange(9):
            iq = 0 if i < 3 else 1 if i < 6 else 2
            for j in xrange(9):
                jq = 0 if j < 3 else 1 if j < 6 else 2
                print i,j
                if b[i][j] != '.':
                    if (b[i][j] in h[i] or b[i][j] in v[j] or b[i][j] in d[(iq,jq)]): 
                        return False
                    h[i].add(b[i][j])
                    v[j].add(b[i][j])
                    d[(iq,jq)].add(b[i][j])
                
        return True
        
