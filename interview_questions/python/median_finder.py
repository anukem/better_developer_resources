# given two sorted arrays of the same length, find the median without joining the arrays together.
import math

def find_median(A, B):
    medB, medA = 0, 0
    while len(A) != 2:
        if A[medA] > B[medB]:
            A = A[0:medA + 1]
            B = B[medB:len(B)]
        elif A[medA] < B[medB]:
            A = A[medA:len(A)]
            B = B[0:medB + 1]

        print(len(A)
        medB = medA
        print(medA)
    if len(A) == 2:
        return math.avg(A) + math.avg(B) / 2
    else:
        return A[0] + B[0] / 2


print(find_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))  # 5.5
print(find_median([1, 3, 5, 7], [2, 4, 6, 8, 1230]))  # 5.5
