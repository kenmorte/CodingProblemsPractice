# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return
        curr = head
        copy = {None:None}
        while curr:
            copy[curr] = RandomListNode(curr.label)
            curr = curr.next
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next
        return copy[head]
