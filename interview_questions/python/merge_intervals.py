# 56. Merge Intervals
# Medium
#
# 5083
#
# 318
#
# Add to List
#
# Share
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    i = 0
    while i < len(intervals) - 1:
        current_start, current_end = intervals[i]
        next_start, next_end = intervals[i + 1]

        if next_start > current_end:
            i += 1
            continue
        elif next_end <= current_end:
            intervals.pop(i + 1)
        elif next_start <= current_end:
            intervals[i] = [current_start, next_end]
            intervals.pop(i + 1)

    return intervals
