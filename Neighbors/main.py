"""
Code Challenge: Implement Neighbors to find the d-neighborhood of a string.
     Input: A string Pattern and an integer d.
     Output: The collection of strings Neighbors(Pattern, d).

"""

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

