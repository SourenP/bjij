from collections import defaultdict
import sys

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.readline().rstrip()
        k, L, t = map(int, f.readline().rstrip().split())
elif len(sys.argv) == 5:
    with open(sys.argv[1]) as f:
        data = f.readline().rstrip()
    k, L, t = map(int, sys.argv[2:])


def ClumpFinding(data, k, L, t):
    k_mers = defaultdict(list)

    for i in range(len(data) - k):
        k_mer = data[i:i+k]
        k_mers[k_mer].append(i)

    def has_clump(locs, L, t, k):
        for i in range(len(locs)):
            if len(locs) - i < t:
                break
            if locs[i+t-1] + k - locs[i] <= L:
                return True
        return False

    clump_k_mers = [k_mer for k_mer, locs in k_mers.items()  if has_clump(locs, L, t, k)]
    return clump_k_mers

clump_k_mers = ClumpFinding(data, k, L, t)

print(" ".join(clump_k_mers))
print(len(set(clump_k_mers)))

