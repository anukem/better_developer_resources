# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []


def two_sum(el, lst, res, found):
    seen = {}
    for val in lst:
        if el - val in seen and (el * -1, val, el - val) not in seen:
            res.append([el * -1, val, el - val])
            seen[(el * -1, val, el - val)] = 1
        else:
            seen[val] = 1
    return res


def three_sum(lst):
    res = []
    seen = {}
    lst = sorted(lst)
    if not lst:
        return []
    elif len(lst) < 3:
        return []
    else:
        for i, el in enumerate(lst):
            if el not in seen:
                two_sum(el * -1, lst[i + 1 :], res, seen)
                seen[el] = 1

    return res


# tested on leetcode
