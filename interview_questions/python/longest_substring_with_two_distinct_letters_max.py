# Given  the same string, find the length of the longest substring T that contains at most 2 distinct characters.
# For example, Given s = “eceba”,
# T is "ece" which its length is 3.

def two_distinct_length(s):
    j = 0

    longest = 1

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    mapping = {}

    count = 0

    while j != len(s):
        if s[j] not in mapping:
            mapping[s[j]] = j, 1
            if len(mapping) > 2:
                mapping.pop(min(mapping.items(), key=lambda x: x[1][0])[0])
        else:
            mapping[s[j]] = (j, mapping[s[j]][1] + 1)

        count = max(count, sum([x[1] for x in mapping.values()]))
        j += 1

    return count
