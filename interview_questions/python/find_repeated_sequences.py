def find_sequences(s):

    counter = {}

    if len(s) <= 10:
        return []

    for i in range(len(s) - 10):
        counter[s[i : i + 11]] = counter.get(s[i : i + 11], 0) + 1

    sequences = []
    for seq, count in counter.items():
        if count > 1:
            sequences.append(seq)

    return sequences
