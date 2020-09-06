# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
#
#  */


def merge_intervals(arr, index):
    if index == len(arr) - 1:
        return arr

    if arr[index + 1][1] < arr[index][1]:
        arr[index + 1] = arr[index]
        arr[index] = None
    elif arr[index + 1][0] < arr[index][1]:
        arr[index + 1] = (arr[index][0], arr[index + 1][1])
        arr[index] = None

    return merge_intervals(arr, index + 1)


def partition_string(s):
    arr = []
    seen = {}

    for index, val in enumerate(s):
        if val not in seen:
            seen[val] = (index, index)
        else:
            seen[val] = (seen[val][0], index)

    for key in seen:
        arr.append(seen[key])

    arr = merge_intervals(arr, 0)
    arr = [x for x in arr if x is not None]
    arr = list(map(lambda x: x[1] - x[0] + 1, arr))

    return arr


partition_string("ababcbacadefegdehijhklij")

# tested on leetcode.
