# https://leetcode.com/problems/distribute-candies/#/description

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = dict()
        for candy in candies:
            if candy not in kinds:
                kinds[candy] = 1
            else:
                kinds[candy] += 1
        
        different_kinds_sister_has = len(kinds) # give sister one of each kind
        for kind in kinds:
            kinds[kind] -= 1
        
        number_of_candies_left_for_brother = sum(kinds.values())
        
        if different_kinds_sister_has <= number_of_candies_left_for_brother:
            return different_kinds_sister_has
            
        while different_kinds_sister_has != number_of_candies_left_for_brother:
            # give one of sister's candy to brother
            different_kinds_sister_has -= 1
            number_of_candies_left_for_brother += 1
            
        return different_kinds_sister_has
