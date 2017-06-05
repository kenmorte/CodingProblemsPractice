# https://leetcode.com/problems/intersection-of-two-linked-lists/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # Initial, brute-force solution -- hashmap of nodes+indices for each node in both A and B
        #   Find the common nodes --> find the least index --> get the node with the least index
        
        hash_mapA = dict()
        hash_mapB = dict()
        
        currentA = headA
        current_indexA = 0
        
        currentB = headB
        current_indexB = 0
        
        while currentA is not None:
            hash_mapA[currentA] = current_indexA
            currentA = currentA.next
            current_indexA += 1
        
        while currentB is not None:
            hash_mapB[currentB] = current_indexB
            currentB = currentB.next
            current_indexB += 1
            
            
        result = None
        min_index_sum = float('inf')
        
        for nodeA in hash_mapA:
            if nodeA in hash_mapB:
                indexA = hash_mapA[nodeA]
                indexB = hash_mapB[nodeA]
                index_sum = indexA + indexB
                
                if index_sum < min_index_sum:
                    result = nodeA
                    min_index_sum = index_sum
                    
        return result
        
        
        
