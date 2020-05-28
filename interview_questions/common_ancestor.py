
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

