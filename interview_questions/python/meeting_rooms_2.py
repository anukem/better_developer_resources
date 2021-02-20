# Description
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Have you met this question in a real interview?
# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
# Example2

# Input: intervals = [(2,7)]
# Output: 1
# Explanation:
# Only need one meeting room


class Interval(object):
    def __init__(self, interval):
        self.interval = interval
        pass

    def __lt__(self, other):
        return self.interval[1] < other.interval[1]


def minimum_rooms_needed(intervals):
    intervals.sort()
    from heapq import heappush, heappop

    minheap = []

    if not intervals or not len(intervals):
        return 0

    heappush(minheap, Interval(intervals[0]))
    for current_start, current_end in intervals[1:]:
        earliest_start, earliest_end = heappop(minheap).interval

        if earliest_end < current_end:
            earliest_end = current_end
        else:
            heappush(minheap, Interval([current_start, current_end]))

        heappush(minheap, Interval([earliest_start, earliest_end]))

    return len(minheap)


def test_1():
    assert minimum_rooms_needed([[0, 30], [5, 10], [15, 20]]) == 2


def test_2():
    assert minimum_rooms_needed([[0, 30]]) == 1


def test_3():
    assert minimum_rooms_needed([[0, 30], [1, 5], [2, 4]]) == 3