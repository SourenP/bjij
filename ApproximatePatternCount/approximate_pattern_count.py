def HammingDistance(p, q):
    if len(p) != len(q):
        return -1
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d


# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Text, Pattern, d):
    count = 0 # initialize count variable

    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count += 1
    # your code here
    return count


# Insert your HammingDistance function on the following line.
