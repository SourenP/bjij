"""
Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
     Input: A string Text, an integer k, and a 4 x k matrix Profile.
     Output: A Profile-most probable k-mer in Text.
"""

def pr_prof(k_mer, profile):
	p = 1.0
	for i in range(len(k_mer)):
		p = p * profile[k_mer[i]][i]
	return p


# Write your ProfileMostProbableKmer() function here along with any subroutines you need.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
	k_mer_p = []
	for i in range(len(text) - k + 1):
		k_mer = text[i:i+k]
		k_mer_p.append((k_mer, pr_prof(k_mer, profile)))
	m = max(k_mer_p, key=lambda x: x[1])
	return m[0]
