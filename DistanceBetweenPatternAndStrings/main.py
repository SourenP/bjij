
def hammingdistance(p, q):
    if len(p) != len(q):
        return -1
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d


# Write your DistanceBetweenPatternAndStrings() function here along with any subroutines that you need.
# dna is a list of strings.
def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    
    for text in dna:
        h_d = k+1
        for i in range(len(text) - k + 1):
            k_mer = text[i:i+k]
            if h_d > hammingdistance(pattern, k_mer):
                h_d = hammingdistance(pattern, k_mer)
        distance += h_d
    return distance
