# https://leetcode.com/problems/beautiful-arrangement/description/

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        
        # Build our 2-d table of valid numbers at indices
        table = [[False for j in range(N)] for i in range(N)]
        for n in range(N):
            for i in range(N):
                table[n][i] = (n+1) % (i+1) == 0 or (i+1) % (n+1) == 0
        result = 0
        
        for n in range(N):
            taken_ns = {n}
            
            # Look for all possible combinations at with 'n' starting at index 1
            result += self.check_next_index(table, taken_ns, 1, N)
            
        return result
                
    def check_next_index(self, table, taken_ns, i, N):
        combinations = 0
        for n in range(N):
            # If is valid number at this index
            if n not in taken_ns and table[n][i]:
                # At the last index and found a possible combination
                if i == N - 1:
                    # print('combination = ', [a+1 for a in taken_ns + [n]])
                    return 1
                
                # Not at the last index yet, need to check next index for possible combinations
                taken_ns.add(n)
                combinations += self.check_next_index(table, taken_ns, i + 1, N)
                taken_ns.remove(n)
        return combinations
            
                
        
        
