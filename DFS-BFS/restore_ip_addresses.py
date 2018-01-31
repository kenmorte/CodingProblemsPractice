# https://leetcode.com/problems/restore-ip-addresses/description/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4: return []
        res = []
        self.dfs([], s, res)
        return res
        
    def dfs(self, ip, s, res):
        if len(ip) == 4: 
            if not s: res.append('.'.join(ip))
            return
        if not s: return
        
        possibleIPs = []
        if len(s) >= 1: possibleIPs.append(s[:1])
        if len(s) >= 2: possibleIPs.append(s[:2])
        if len(s) >= 3: possibleIPs.append(s[:3])
        if s[0] == '0': possibleIPs = ['0']
        
        for possibleIP in possibleIPs:
            if int(possibleIP) <= 255:
                ip.append(possibleIP)
                self.dfs(ip, s[len(possibleIP):], res)
                ip.pop()
        
        
