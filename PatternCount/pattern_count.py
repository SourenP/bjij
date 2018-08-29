with open('dataset_2_7.txt') as f:
    data = f.readline().rstrip()
    pattern = f.readline().rstrip()

print(data)
print(pattern)


def PatternCount(data, pattern):
    count = 0
    for i in range(len(data) - len(pattern) + 1):
        if data[i:i+len(pattern)] == pattern:
            count += 1
    return count
        
print(PatternCount(data, pattern))
