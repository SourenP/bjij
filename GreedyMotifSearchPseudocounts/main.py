"""
Code Challenge: Implement GreedyMotifSearch.
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna,k,t).
   If at any step you find more than one Profile-most probable k-mer in a given string, use the
   one occurring first.
"""


def score_motifs(motifs, k): 
    score = 0
    for i in range(k):
        totals = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(len(motifs)):
            totals[motifs[j][i]] += 1
        score += sum(totals.values()) - max(totals.values()) 
    return score


def pr_prof(k_mer, profile):
	p = 1.0
	for i in range(len(k_mer)):
		p = p * profile[k_mer[i]][i]
	return p


def ProfileMostProbableKmer(text, k, profile):
	k_mer_p = []
	for i in range(len(text) - k + 1):
		k_mer = text[i:i+k]
		k_mer_p.append((k_mer, pr_prof(k_mer, profile)))
	m = max(k_mer_p, key=lambda x: x[1])
	return m[0]


def form_profile(motifs, k, pseudocount):
    profile = { 'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(k):
        totals = {'A': pseudocount, 'C': pseudocount, 'G': pseudocount, 'T': pseudocount}
        for j in range(len(motifs)):
            totals[motifs[j][i]] += 1
        for k in profile:
            profile[k].append(float(totals[k])/sum(totals.values()))
    return profile
            

# Implement GreedyMotifSearch() below along with any subroutines that you need.
# Your function should return a list of strings.
def GreedyMotifSearchWithPseudocounts(dna, k, t, pseudocount):
    best_motifs = [s[:k] for s in dna] 
    motifs = []
    for i in range(len(dna[0]) - k + 1):
        motif_0 = dna[0][i:i+k]
        motifs.append(motif_0)
        for i in range(1, t):
            profile = form_profile(motifs, k, pseudocount)
            motifs.append(ProfileMostProbableKmer(dna[i], k, profile))
        if score_motifs(motifs, k) < score_motifs(best_motifs, k):
            best_motifs = motifs
        motifs = []
    return best_motifs
