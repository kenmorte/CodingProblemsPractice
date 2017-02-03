# anagram = both strings must contain the same exact letters in the same exact frequency
#   --> the length of both strings must be equal

# we'll have two strings --> both can be any length, and can be different
#   to make into anagram, we have to remove characters from the longer string
#
#   how will we know which characters to delete?
#       keep an internal dict of both strings w/key = char, and value = charcount
#       iterate through the longer dictionary, check each character count
#           if the the other dict doesn't have the char, then delete all from the current dict (and change the str)
#               delete #currentdict
#           elif the other dict has less chars, delete some from the current dict (and change the str)
#               delete (#currentdict - #otherdict) characters
#           elif the other dict has more chars, delete some from that dict (and change the str)
#               delete (#otherdict - #currentdict) characters
#           else if they're equal --> perfect! go to next iteration

def number_needed(a, b):
    nA = len(a); nB = len(b)
    map_a = {c : a.count(c) for c in a}; map_b = {c : b.count(c) for c in b};
    
    longer_dict = map_a if nA > nB else map_b
    shorter_dict = map_b if longer_dict == map_a else map_a
    
    count = 0
    for c in set(longer_dict.keys()):
        if c not in shorter_dict:
            count += longer_dict[c]
            longer_dict.pop(c)
            
        elif longer_dict[c] > shorter_dict[c]:
            count += longer_dict[c] - shorter_dict[c]
            longer_dict[c] = shorter_dict[c]
            
        elif longer_dict[c] < shorter_dict[c]:
            count += shorter_dict[c] - longer_dict[c]
            longer_dict[c] = shorter_dict[c]
            
    for c in shorter_dict:
        if c not in longer_dict:
            count += shorter_dict[c]
            
        elif shorter_dict[c] > longer_dict[c]:
            count += shorter_dict[c] - longer_dict[c]
            
        elif shorter_dict[c] < longer_dict[c]:
            count += longer_dict[c] - shorter_dict[c]
    
    return count
    

a = input().strip()
b = input().strip()

print(number_needed(a, b))
