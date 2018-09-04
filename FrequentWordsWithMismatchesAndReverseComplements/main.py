"""
Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
      Input: A DNA string Text as well as integers k and d.
      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Pattern)
      over all possible k-mers.

"""

from collections import Counter
from itertools import takewhile
import operator


comp = {'T': 'A', 'G': 'C', 'A': 'T', 'C': 'G'}

def ReverseComplement(data):
    return "".join(reversed([comp.get(x) for x in data]))

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

def FrequentWordsWithMismatchesAndReverseComplements(data, k, d):
    freq = Counter()

    for i in range(len(data) - k + 1):
        k_mer = data[i:i+k]
        for n in Neighbors(k_mer, d):
            freq[n] += 1
            freq[ReverseComplement(n)] += 1

    items = freq.most_common()
    max_ = items[0][1]
    top_items = list(takewhile(lambda x: x[1]==max_,  items))
    top_words = sorted([i[0] for i in top_items])
    return top_words
