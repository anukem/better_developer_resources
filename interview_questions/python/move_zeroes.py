# 283. Move Zeroes
# Easy
#
# 4079
#
# 130
#
# Add to List
#
# Share
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Accepted
# 889,756
# Submissions
# 1,536,286
#
#  0 1 2 2
# 1 0 2 2
#
# find a zero
# move it to the end of the array
# repeat until theres no zeroes left to move


def swap_zero_to_the_end(arr, i):
    for j in range(i + 1, len(arr)):
        tmp = arr[j]
        arr[j] = 0
        arr[i] = tmp
        i += 1


def find_next_zero(arr):
    i = 0
    while arr[i] != 0:
        i += 1
    return i


# solution is n squared where n is the number of elements
def move_zeroes(arr):
    # return the arr modified in place with the zeros at the end

    num_of_zeroes = arr.count(0)

    while num_of_zeroes > 0:
        i = find_next_zero(arr)
        swap_zero_to_the_end(arr, i)
        num_of_zeroes -= 1
    return arr
