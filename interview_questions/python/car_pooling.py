# https://leetcode.com/problems/car-pooling/
def car_pooling(trips, capacity):
    trips.sort(key=lambda x: x[1])

    timeline = {}
    for trip in trips:
        for t in range(trip[1], trip[2]):
            timeline[t] = timeline.get(t, 0) + trip[0]

    for t in timeline:
        if timeline[t] > capacity:
            return False
    return True


