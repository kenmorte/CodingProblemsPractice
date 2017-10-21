# https://leetcode.com/problems/queue-reconstruction-by-height/description/

class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []
        
        k_map = dict()
        heights = sorted(list(set(p[0] for p in people)))
        result = []
        
        for p in people:
            if p[0] not in k_map:
                k_map[p[0]] = [p[1]]
            else:
                k_map[p[0]] += [p[1]]
        
        for h in heights[::-1]:
            for k in sorted(k_map[h]):
                print h, k
                result.insert(k, [h, k])
        return result
            
