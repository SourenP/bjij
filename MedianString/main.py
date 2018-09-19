"""
Code Challenge: Implement MedianString.
     Input: An integer k, followed by a collection of strings Dna.
     Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern. (If there are multiple such strings Pattern,
     then you may return any one.)
"""

letters = {'A', 'C', 'G', 'T'}

def HammingDistance(p, q):
    if len(p) != len(q):
        return -1
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d


def KMers(s, k):
    return [s[i:i+k] for i in range(len(s) - k + 1)]


def d_s(pattern , s):
    k = len(pattern)
    return min([HammingDistance(pattern, s[i:i+k]) for i in range(len(s) - k + 1)])


def d_l(pattern, l):
    return sum([d_s(pattern, s) for s in l])

def Neighbors(pattern, d):
    if len(pattern) == 0:
        return [pattern]
    if d == 0:
        return [pattern]

    mutations = []
    first_l = pattern[:1]
    mutations += [first_l + n for n in Neighbors(pattern[1:], d)]
    for l in letters - set(first_l):
        mutations += [l + n for n in Neighbors(pattern[1:], d-1)]

    return mutations

# Write your MedianString() function here, along with any subroutines that you need.
# You should return your answer as a string.
def MedianString(dna, k):
    k_mers = []
    for s in dna:
        k_mers += KMers(s, k)

    k_mers_n = []
    for k_mer in set(k_mers):
        k_mers_n += Neighbors(k_mer, k)

    distance = 2**32 # inf
    for k_mer in set(k_mers_n):
        d = d_l(k_mer, dna)
        if distance > d:
            distance = d
            median = k_mer
    return median


def MedianStringCandidates(dna, k, c):
    distance = 2**32 # inf
    for k_mer in set(c):
        d = d_l(k_mer, dna)
        print(k_mer, d)
        if distance > d:
            distance = d
            median = k_mer
    return median

