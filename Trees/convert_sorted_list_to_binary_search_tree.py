# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = self.linkedListToArray(head)
        return self.sortedArrayToBST(arr)
        
    def sortedArrayToBST(self, arr):
        if not arr: return None
        if len(arr) == 1: return TreeNode(arr[0])
        if len(arr) == 2:
            root = TreeNode(arr[1])
            child = TreeNode(arr[0])
            if arr[0] <= arr[1]: root.left = child
            else: root.right = child
            return root
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root
    
    def linkedListToArray(self, head):
        res = []
        while head:
            res += [head.val]
            head = head.next
        return res
