from collections import Counter
from itertools import takewhile
import operator

with open('dataset_test.txt') as f:
    data = f.readline().rstrip()
    count = int(f.readline().rstrip())


def FrequentWords(data, count):
    freq = Counter()

    for i in range(len(data) - count + 1):
        freq[data[i:i+count]] += 1

    items = freq.most_common()
    max_ = items[0][1]
    top_items = list(takewhile(lambda x: x[1]==max_,  items))
    top_words = sorted([i[0] for i in top_items])
    return top_words

print((' ').join(FrequentWords(data, count)))
