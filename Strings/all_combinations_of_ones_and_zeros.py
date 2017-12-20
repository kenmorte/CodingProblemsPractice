# Write a program that takes a string of 1's and 0's and ?'s and outputs all possible combinations of 1's and 0's where the ?'s are replaced with 1's and 0’s.
# NOTE: Asked by Yahoo! on 12/19/2017

# 0, 1, ?
# empty str, all question marks
# input str
# output [[str]]

# 1??
# 100
# 101
# 110
# 111

def replaceAll(s):
    if not s: return []
    res = []
    dfs(s, '', res)
    return res
    
def dfs(s, curr, res):
    if not s:
        res.append(curr)
        return
    if s[0] in {'0','1'}: 
        dfs(s[1:], curr+s[0], res)
    else:
        dfs(s[1:], curr+'0', res)
        dfs(s[1:], curr+'1', res)

# res = [100, 101]
# 1??
#    ?? --> call this w/ 0 and w/1, curr = 1
#        ? --> curr = 10, call w/01
#            '' --> curr = 100
#            '' --> curr = 101
#
# TB long
