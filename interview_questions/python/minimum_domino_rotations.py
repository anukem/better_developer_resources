def minimum_rotations(A, B):

    if len(A) != len(B):
        return -1

    if not A or not B:
        return -1

    candidates = set()
    candidates.add(A[0])
    candidates.add(B[0])

    counter = {x: (0, 0) for x in candidates}

    for i in range(len(A)):
        if A[i] not in candidates and B[i] not in candidates:
            return -1

        candidates = [el for el in candidates if el in [A[i], B[i]]]
        for candidate in candidates:
            if candidate == A[i]:
                counter[candidate] = (
                    counter.get(candidate)[0] + 1,
                    counter.get(candidate)[1],
                )
            if candidate == B[i]:
                counter[candidate] = (
                    counter.get(candidate)[0],
                    counter.get(candidate)[1] + 1,
                )

    candidate = candidates.pop()

    res, arr = (
        (counter.get(candidate)[0], A)
        if counter.get(candidate)[0] > counter.get(candidate)[1]
        else (counter.get(candidate)[1], B)
    )

    return min(res, len(arr) - res)


print(minimum_rotations([1, 2, 1, 1, 1, 2, 2, 2], [2, 1, 2, 2, 2, 2, 2, 2]))  # => 1
