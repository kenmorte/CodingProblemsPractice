# https://leetcode.com/problems/employee-importance/description/

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employee_map = dict()
        for employee in employees:
            employee_map[employee.id] = employee
        
        result = 0
        ids_to_check = [id]
        while len(ids_to_check) > 0:
            employee = employee_map[ids_to_check.pop(0)]
            ids_to_check += employee.subordinates
            result += employee.importance
        return result
