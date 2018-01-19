# https://leetcode.com/problems/my-calendar-i/description/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class MyCalendar(object):

    def __init__(self):
        # O(n) solution
        # self.events = []
        
        # O(logn) solution
        self.root = None

    def book(self, s, e):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode((s,e))
            return True
        return self.binaryInsert(self.root, s, e)
        
    def binaryInsert(self, root, s, e):
        ps, pe = root.val
        
        if (ps <= s and s < pe) or (ps < e and e <= pe) or (s < ps and e > ps):
            return False
        
        if e <= ps:
            if not root.left: 
                root.left = TreeNode((s,e))
                return True
            else: return self.binaryInsert(root.left, s, e)
        
        if s >= pe:
            if not root.right: 
                root.right = TreeNode((s,e))
                return True
            else: return self.binaryInsert(root.right, s, e)
        
        
        # O(n) brute force approach
        # if not self.events:
        #     self.events += [(s,e)]
        #     return True
        # for ps, pe in self.events:
        #     if (ps <= s and s < pe) or (ps < e and e <= pe) or (s < ps and e > ps):
        #         return False
        # inserted = False
        # index_to_insert = -1
        # for i, event in enumerate(self.events):
        #     ps, pe = event
        #     if s >= pe:
        #         index_to_insert = i
        #         break
        # if not inserted: self.events.insert(index_to_insert+1,(s,e))
        # return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
