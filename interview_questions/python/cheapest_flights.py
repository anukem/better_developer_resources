# 787. Cheapest Flights Within K Stops Medium 2203 74 Add to List
#
# Share
# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
# Constraints:
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.


def find_cheapest_flight(flight_map, src, dst, k, cost):
    if src == dst and k >= 0:
        return cost
    elif k == 0:
        return float("inf")

    neighbors = flight_map[src]
    total_cost = []
    for new_destination, c in neighbors:
        total_cost.append(
            find_cheapest_flight(flight_map, new_destination, dst, k - 1, cost + c)
        )

    return min(total_cost)


def cheapestFlights(flights, src, dst, k):
    flight_map = {}
    for (s, d, cost) in flights:
        if s in flight_map:
            flight_map[s].append((d, cost))
        else:
            flight_map[s] = [(d, cost)]
    answer = find_cheapest_flight(flight_map, src, dst, k + 1, 0)
    return -1 if answer == float("inf") else answer


cheapestFlights([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
