
# given a binary tree, determine the first most common ancestor of two nodes

tree = { 1: [], 2: [1, 4], 4: [6, 8], 9: [], 10: [], 6: [9, 10], 8: [11, 12], 11: [], 12: []}

#    2
#  1   4
#    6     8
#   9 10 11 12

def common_ancestor(left, right, node):
    if node == left:
        return True, False
    elif node == right:
        return False, True

    if tree[node] == []:
        return False, False

    left_found, _ = common_ancestor(left, right, tree[node][0])
    _, right_found = common_ancestor(left, right, tree[node][1])

    if left_found and right_found:
        print(node)
        return True, True
    else:
        return left_found, right_found



print(common_ancestor(9, 12, 2))

#
# #
# # Your previous Python 3 content is preserved below:
# #
# # /**
# # * A Directed Acyclic Graph is represented in a list of pairs, and the first element of the pair has a directed link to the second element. All
# # * elements in each pairs are uniquely represented by a positive number.
# # * For example, [[1, 2], [3, 4], [1, 3], [5, 4]] represents a graph like this:
# # *
# # * Write a function, given two numbers A, and B, return true if and only if the graph contains at least one common ancestor.
# # */
# #
#


def common_ancestor(A, B, pairs):
    mapping = {}
    for ancestor, child in pairs:
        mapping[child] = mapping.get(child, []) + [ancestor]


    def add_ancestors(node, s):
        for ancestor in mapping.get(node, []):
            s.add(ancestor)
            add_ancestors(ancestor, s)

        return s

    ancestors_a = add_ancestors(A, set())
    ancestors_b = add_ancestors(B, set())

    if (len(ancestors_a.intersection(ancestors_b)) >= 1 or
        A in ancestors_b or
        B in ancestors_a):
            return True
    else:
        return False


import pytest

def test_1():
    assert common_ancestor(2, 3 , [[1, 2], [3, 4], [1, 3], [5, 4]] ) == True

def test2():
    assert common_ancestor(2, 1 , [[1, 2], [3, 4], [1, 3], [5, 4]] ) == True

def test3():
    assert common_ancestor(1, 5 , [[1, 2], [3, 4], [1, 3], [5, 4]] ) == False

pytest.main()
