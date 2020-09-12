# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


def combination_sum(n, k):
    res = []

    def helper(n, k, options=[x + 1 for x in range(9)], combination=[]):
        if k == 0 and n == 0:
            res.append(combination)
            return
        for i, el in enumerate(options):
            helper(n - el, k - 1, options[i + 1 :], combination + [el])

    helper(n, k)
    return res


# tested on leetcode
