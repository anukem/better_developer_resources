# # Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# #
# # You may assume that the intervals were initially sorted according to their start times.
# #
# # Example 1:
# #
# # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# # Output: [[1,5],[6,9]]
# # Example 2:
# #
# # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# # Output: [[1,2],[3,10],[12,16]]
# # Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def merge_intervals(intervals, new_interval):
    intervals.append(new_interval)
    intervals = sorted(intervals)

    index = 0
    while index < len(intervals) - 1:
        interval = intervals[index]
        next_interval = intervals[index + 1]
        next_start, next_end = next_interval
        current_start, current_end = interval

        if next_start > current_end:
            index += 1
            continue
        elif current_end > next_end:
            intervals.pop(index + 1)
        elif next_start <= current_end:
            intervals[index] = [current_start, next_end]
            intervals.pop(index + 1)

    return intervals

# tested on leetcode
