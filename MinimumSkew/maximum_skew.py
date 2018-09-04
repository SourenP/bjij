def MaximumSkew(genome):
    skew = [0]
    s = 0
    for i in range(len(genome)):
        if genome[i] == 'G':
            s += 1
        elif genome[i] == 'C':
            s -= 1
        skew.append(s)
    s_min = max(skew)
    return [i for i, j in enumerate(skew) if j == s_min]
