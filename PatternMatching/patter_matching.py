import sys

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        pattern = f.readline().rstrip()
        data = f.readline().rstrip()
elif len(sys.argv) == 3:
    with open(sys.argv[1]) as f:
        data = f.readline().rstrip()
    pattern = sys.argv[2]
else:
    exit(0)


# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(pattern, data):
    indices = []

    for i in range(len(data) - len(pattern) + 1):
        if data[i:i+len(pattern)] == pattern:
            indices.append(str(i))
    return indices

print(" ".join(PatternMatching(pattern, data)))
