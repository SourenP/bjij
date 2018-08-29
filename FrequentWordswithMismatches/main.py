"""
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
"""
letters = set(['A', 'C', 'G', 'T']) 

def HammingDistance(p, q):
    if len(p) != len(q):
        return -1
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

def produce_mutations(pattern, d):
    mutations = [pattern]
    produce_mutations_r(mutations, d)

def produce_mutations_r(pattern, t):
    "ABC, 2"
    if t < 0 or len(pattern) == 0:
        return []

    print(pattern, t)

    lefts = []
    rights = []
    for i in range(len(pattern)-1):
        for l in letters - set(pattern[i]):
            lefts.append(pattern[:i] + l)
            rights.append(produce_mutations_r(pattern[i+1:], t-1))

    out = []
    for i, l in enumerate(lefts):
        for r in rights[i]:
            out.append(l+r)
    print(out)
    return out 
    
# Write your FrequentWordsWithMismatches() function here, along with any subroutines you need.
# Your function should return a list.
def FrequentWordsWithMismatches(Text, k, d):
    pass    
