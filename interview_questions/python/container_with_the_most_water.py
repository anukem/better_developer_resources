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

class Solution:
    """
    Prompt: Container With Most Water


    Solution Deep-Dive.
    Helpful Video: https://youtu.be/UuiTKBwPgAo

    This equation looks for the largest possible area. In order to do that, the biggest limiting factor
    will always be the smaller pillar height. Knowing that, we start with the largest range i=0, j=arr.size()
    and calculate area. We keep iterating until i == j. Once done, we return the max value computed.

    Brute Force:
    - Loop through everything and get the max

    Logical Breakdown:
    - With each iteration the algorithm, there are a few considerations we make.
      - There (may) exist a larger area that can be computed.
      - The distance will continue to get smaller, so the only assisting factor is height.

    - Knowing these things we can assume that with each iteration, we can only stand to gain more area if
    there is a higher height in at the indices in-between.
    - The decision for which pillar to move stems from one core belief. If you iterate the smaller pillar
    you lose the likelihood of

    Small Optimizations:
    - fold function into maxArea function
    - avoid copying a reference to the list on init
    """
    def _maxAreaBrute(self):
        """Brute Force O(n**2)"""
        max_val = 0
        i = 0
        while i < len(self.heights):
            j = i+1
            while j < len(self.heights):
                max_val = max(max_val, self._computeArea(i, j))

    def _computeArea(self, index1: int, index2: int) -> int:
        """Convenience function to compute area"""
        return min(self.heights[index1], self.heights[index2]) * abs(index1-index2)

    def _edgeCompare(self) -> int:
        # Initialize list to start at largest range possible
        left_index = 0
        right_index = len(self.heights) - 1
        max_val = 0
        # Iteratively close in on the list until ranges pass one another
        while left_index < right_index:
            max_val = max(max_val, self._computeArea(left_index, right_index))
            # if the left pillar is taller, iterate left right one
            if self.heights[left_index] < self.heights[right_index]:
                left_index+=1
            # Otherwise increment the right index left one
            else:
                right_index-=1
        return max_val

    def maxArea(self, height: List[int]) -> int:
        self.heights = height
        # return self._maxAreaBrute()
        return self._edgeCompare()
