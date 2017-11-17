# https://leetcode.com/problems/minimum-index-sum-of-two-lists/#/description

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        # Two hashmaps --> one for list1 and another for list2
        #   Keep track of the index for each item in the list
        # Initialize result list and the min_index_sum = infinity
        # Iterate through one of the hashmaps
        #   Check if that restaurant is in the other hashmap --> O(1)
        #       If it is, calculate the index_sum
        #           If the index_sum == min_index_sum --> add it the result list
        #           Else if the index_sum < min_index_sum --> empty out the result, add in this restaurant, set new min_index_sum
        #           Else if the index sum is > min index sum --> dont do anything
        # Return result
        
        # ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        # ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] --> GOOD
        
        # ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        # ["KFC", "Shogun", "Burger King"]
        
        hash_map1 = dict()
        hash_map2 = dict()
        
        for i in range(len(list1)): # get map of indices for first list
            hash_map1[list1[i]] = i
            
        
        for i in range(len(list2)): # get map of indices for second list
            hash_map2[list2[i]] = i
            
        result = []
        min_index_sum = float('inf')
        
        for rest in hash_map1:
            if rest in hash_map2:
                index1 = hash_map1[rest]
                index2 = hash_map2[rest]
                
                index_sum = index1 + index2
                
                if index_sum == min_index_sum:
                    result.append(rest)
                elif index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [rest]
                
        return result
            
