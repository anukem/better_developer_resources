# given two strings, determine if one is a permutation of the other

# time => O(aloga + blogb)
def check_permutation(a, b):
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)

    if (a == b):
        return True
    else:
        return False


def create_map(word):
    seenA = {}
    for letter in word:
        if letter in seenA:
            seenA[letter] += 1
        else:
            seenA[letter] = 1
    return seenA


# time => O(a + b)
def check_permutation_with_map(a, b):
    if len(a) != len(b):
        return False
    mapA = create_map(a)
    mapB = create_map(b)

    for key in mapA:
        try:
            if mapA[key] != mapB[key]:
                return False
        except:
            return False
    return True


print(check_permutation_with_map("some", "omes"))
