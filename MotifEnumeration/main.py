"""
Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches.

Code Challenge: Implement MotifEnumeration (reproduced below).
     Input: Integers k and d, followed by a collection of strings Dna.
     Output: All (k, d)-motifs in Dna.
"""

from collections import Counter
from collections import defaultdict
from itertools import takewhile
import operator

letters = {'A', 'C', 'G', 'T'}

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

def WordsWithMismatches(data, k, d):
    k_mers = set()

    for i in range(len(data) - k + 1):
        k_mer = data[i:i+k]
        for n in Neighbors(k_mer, d):
            k_mers.add(n)

    return k_mers

# Write your MotifEnumeration() function here along with any subroutines you need.
# This function should return a list of strings.
def MotifEnumeration(dna, k, d):
    k_mers = defaultdict(list)

    for i, s in enumerate(dna):
        for k_mer in WordsWithMismatches(s, k, d):
            k_mers[k_mer].append(i)
            
    return [k_mer for k_mer, locs in k_mers.items() if len(locs) == len(dna)]
