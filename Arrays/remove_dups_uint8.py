# NOTE: Asked by Apple 2/22/18

# Don't include duplicate nujmbers
# Can just add to output array
# can be empty

# Set of elements that we've seen - O(n)
# We can just keep a table of 255 booleans - to say if we've seen an element - O(1) space

def removeDups(out, input):
    if not input: return out
    table = [False for _ in xrange(256)]
    for n in input:
        if not table[n]:
            out.append(n)
            table[n] = True
    return out

print removeDups([], [5, 1, 0])

# output = [5, 1, 0, 3]
