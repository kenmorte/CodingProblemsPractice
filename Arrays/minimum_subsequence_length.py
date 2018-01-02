# Asked by Rubrik 1/2/18

'''

haystack = [d, b, e, c, f, g, a, j, k]

# hash set
needles = [a, b, c]

# Find the length of the minimum sub-sequence in haystack
# containing all elements of needles
def find_min(haystack, needles)

> find_min(haystack, needles)
> ? 6
> find_min(haystack, [b, c])
> 3
> find_min(haystack, [a, b])
> 6

Brute force:
- Check all subsequences 
- Check if satisfied having everything needle
- O(n^2) time

Better:
'''
from collections import Counter

def find_min(haystack, needles):
    curr = Counter()
    T = Counter(needles) # {a: 2, b: 1, ...}
    res = float('inf')
    i = j = 0
    while j < len(haystack):
        # advance j until curr is valid compared to T
        curr[haystack[j]] += 1
        
        if len(T) == len(curr) and curr[S[i]] >= T[S[i]]
        
        curr[haystack[i]] -= 1
        if not curr[haystack[i]]: del curr[haystack[i]]
        
    return -1 if res == float('inf') else res


def find_min(haystack, needles):
    if len(haystack) == len(needles): return len(haystack)
    first_index = -1
    counter = 0
    for i in range(len(haystack)):
        c = haystack[i]
        if c in needles:
            if first_index < 0: first_index = i
            counter += 1
            if counter == len(needles):
                return j - i + 1
    return -1 # no solution
    
