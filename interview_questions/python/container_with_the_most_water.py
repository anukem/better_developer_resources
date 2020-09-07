#
# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


def container_with_the_most_water(lines):
    maximum = 0

    i = 0
    j = len(lines) - 1
    while i < j:
        smaller = min(lines[i], lines[j])
        maximum = max(maximum, smaller * (j - i))
        if lines[i] < lines[j]:
            i += 1
        else:
            j -= 1

    return maximum


# tested on leetcode.
