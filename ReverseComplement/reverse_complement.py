with open('dataset_test.txt') as f:
    data = f.readline().rstrip()

comp = {'T': 'A', 'G': 'C', 'A': 'T', 'C': 'G'}

out = "".join(reversed([comp.get(x) for x in data]))

print(out)
