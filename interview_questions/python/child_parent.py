#
# Your previous Plain Text content is preserved below:
#
# Suppose we have some input data describing relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
#
# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
#
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9
#
# parentChildPairs = [
#     [1, 3], [2, 3], [3, 6], [5, 6],
#     [5, 7], [4, 5], [4, 8], [8, 9]
# ]
#
#
# Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.
#
# Sample output:
# Zero parents: 1, 2, 4
# One parent: 5, 7, 8, 9
#
#

parentChildPairs = [
    [1, 3], [2, 3], [3, 6], [5, 6],
    [5, 7], [4, 5], [4, 8], [8, 9]
]

def two_collections(parent_kids):

    hash_of_kids = {}
    for pair in parent_kids:
        child = pair[1]
        parent = pair[0]
        if child in hash_of_kids:
            if hash_of_kids[child] == True:
                hash_of_kids[child] = None
            elif hash_of_kids[child] == False:
                hash_of_kids[child] = True
        else:
            hash_of_kids[child] = True

        if parent not in hash_of_kids:
            hash_of_kids[parent] = False

    collection1 = []
    collection2 = []

    for key in hash_of_kids:
        value = hash_of_kids[key]
        if value == True:
            collection2.append(key)
        elif value == False:
            collection1.append(key)

    return (collection1, collection2)
