# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # O(n) time, O(1) space
        mask = 0
        curr = 0
        chunks = 0
        for i, n in enumerate(arr):
            mask |= 1 << i
            curr |= 1 << n
            if mask == curr: chunks += 1
        return chunks
        
        # O(n^2) time, O(n) space
#         seen = set()
#         chunks = 0
#         for index, n in enumerate(arr):
#             seen.add(n)
            
#             hasSeenAll = True
#             for i in xrange(index+1): 
#                 if i not in seen: 
#                     hasSeenAll = False
#                     break
            
#             if hasSeenAll: chunks += 1
#         return chunks
            
        
        # O(nlogn * 2^n) solution, O(n) space
        # sorted_arr = sorted(arr)
        # return self.dfs(arr[1:], [[arr[0]]], sorted_arr)
    
    # O(nlogn * 2^n) solution
    def dfs(self, arr, chunks, sorted_arr):
        if not arr:
            # sort + concat all our chunks to see if it equals the sorted array
            res = []
            for chunk in chunks: res += sorted(chunk)
            return len(chunks) if res == sorted_arr else float('-inf')
        
        num = arr[0]
        
        chunks[-1].append(num)
        addingToCurrentChunk = self.dfs(arr[1:], chunks, sorted_arr)
        chunks[-1].pop()
        
        chunks.append([num])
        creatingNewChunk = self.dfs(arr[1:], chunks, sorted_arr)
        chunks.pop()
        
        return max(addingToCurrentChunk, creatingNewChunk)
            
