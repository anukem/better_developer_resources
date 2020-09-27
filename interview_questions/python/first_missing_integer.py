# 41. First Missing Positive
# Hard
#
# 4122
#
# 855
#
# Add to List
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# 0000 => 1 => 00001 => 2 => 00011 => 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Follow up:
#
# Your algorithm should run in O(n) time and uses constant extra space.

# move all positive values that have a place in the array to their respective
# positions and check the array afterward to see who is missing

def firstMissingPositive(nums):

    for i in range(len(nums)):
        value = nums[i]
        if 1 >= value >= len(nums) or value == nums[value - 1]:
            continue

        temp = nums[value - 1]
        nums[value - 1] = nums[i]
        nums[i] = temp

    print(nums)
    for i, value in enumerate(nums):
        if value != i + 1:
            return i + 1

    return len(nums) + 1
