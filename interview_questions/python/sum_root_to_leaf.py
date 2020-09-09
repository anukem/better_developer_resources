# Given a binary tree, each node has value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1,
# then this could represent 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
# Return the sum of these numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []

        def sum_root(root, acc):
            res.append(
                acc + str(root.val)
            ) if not root.left and not root.right else None
            sum_root(root.left, acc + str(root.val)) if root and root.left else None
            sum_root(root.right, acc + str(root.val)) if root and root.right else None

        def convert_to_binary(n):
            n = [str(x) for x in n]

            ans = 0
            i = len(n) - 1
            for num in n:
                ans += (2 ** i) * int(num)
                i -= 1
            return ans

        sum_root(root, "")
        return sum([convert_to_binary(x) for x in res])


# tested on leetcode
