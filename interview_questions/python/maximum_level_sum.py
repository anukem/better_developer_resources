
# # Given a binary tree, write a method to return the level that has the maximum sum. In case the tree is empty, return -1
# # Example:
# #        1
# #       / \
# #      2   3
# #     / \ / \
# #    4  5 6  7
# #   /
# #  8
# # Output ==> 2
# # Note: Assume that root is at level 0.


levels = {}

def max_level_sum(root, depth=0):
    if root == None:
        return -1
    levels[depth] = levels.get(depth, 0) + root.val
    if root.left:
        max_level_sum(root.left, depth + 1)
    if root.right:
        max_level_sum(root.right, depth + 1)



def find_max_level(root):
    maxi = max_level_sum(root)
    if maxi == -1:
        return -1
    return max(levels, key=lambda x: x[1])

