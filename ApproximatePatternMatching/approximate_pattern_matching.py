def HammingDistance(p, q):
    if len(p) != len(q):
        return -1
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions
