# https://leetcode.com/problems/shopping-offers/description/

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        if not needs: return 0
        dp = {tuple(0 for _ in needs):0}
        return self.cost(needs, price, special, dp)
    
    def cost(self, needs, price, special, dp):
        if any(itemCount < 0 for itemCount in needs): return float('inf')
            
        Tneeds = tuple(needs)
        if Tneeds in dp: return dp[Tneeds]
        
        cost = float('inf')
        
        for offer in special:
            offerCost = offer[-1]
            
            negativeNeed = False
            for item, numberOfItem in enumerate(offer[:len(offer)-1]):
                needs[item] -= numberOfItem
                negativeNeed = negativeNeed or needs[item] < 0
                
            if not negativeNeed: cost = min(cost, offerCost + self.cost(needs, price, special, dp))
            
            for item, numberOfItem in enumerate(offer[:len(offer)-1]):
                needs[item] += numberOfItem
                
        noSpecial = 0
        for item, numberOfItem in enumerate(needs):
            if numberOfItem > 0: # Calculating minimum cost of spending at each individual item
                noSpecial += needs[item] * price[item]
        cost = min(cost, noSpecial)
        
        dp[Tneeds] = cost
        return dp[Tneeds]
